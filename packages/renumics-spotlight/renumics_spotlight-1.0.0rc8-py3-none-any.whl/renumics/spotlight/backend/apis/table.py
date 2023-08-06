"""
table api endpoints
"""
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, List

from fastapi import APIRouter, Request
from fastapi.responses import Response, ORJSONResponse
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from renumics.spotlight.dtypes.typing import get_column_type_name
from renumics.spotlight.licensing import (
    LicensedFeature,
    username,
    verify_license_or_exit,
)

from renumics.spotlight.typing import PathType

from renumics.spotlight.backend import create_datasource
from ..exceptions import InvalidPath
from ..data_source import (
    Column as DatasetColumn,
    DataSource,
    sanitize_values,
    idx_column,
    last_edited_at_column,
    last_edited_by_column,
)


class Column(BaseModel):
    """
    a single table column
    """

    # pylint: disable=too-few-public-methods

    name: str
    index: Optional[int]
    hidden: bool
    editable: bool
    optional: bool
    role: str
    values: List[Any]
    references: Optional[List[bool]]
    y_label: Optional[str]
    x_label: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    categories: Optional[Dict[str, int]]
    embedding_length: Optional[int]

    @classmethod
    def from_dataset_column(cls, column: DatasetColumn) -> "Column":
        """
        Instantiate column from a dataset column.
        """
        return cls(
            name=column.name,
            index=column.order,
            hidden=column.hidden,
            editable=column.editable,
            optional=column.optional,
            role=get_column_type_name(column.type),
            values=sanitize_values(column.values),
            references=sanitize_values(column.references),
            x_label=column.x_label,
            y_label=column.y_label,
            description=column.description,
            tags=column.tags,
            categories=column.categories,
            embedding_length=column.embedding_length,
        )


# pylint: disable=too-few-public-methods
class Table(BaseModel):
    """
    a table slice
    """

    uid: str
    filename: str
    columns: List[Column]
    max_rows_hit: bool
    max_columns_hit: bool
    generation_id: int


router = APIRouter()


@router.get(
    "/",
    response_model=Table,
    response_class=ORJSONResponse,
    tags=["table"],
    operation_id="get_table",
)
def get_table(request: Request) -> ORJSONResponse:
    """
    table slice api endpoint
    """
    table: Optional[DataSource] = request.app.data_source
    verify_license_or_exit()
    if table is None:
        return ORJSONResponse(
            Table(
                uid="",
                filename="",
                columns=[],
                max_rows_hit=False,
                max_columns_hit=False,
                generation_id=-1,
            ).dict()
        )
    spotlight_license: LicensedFeature = request.app.spotlight_license

    columns = table.get_columns()
    max_columns_hit = False
    if spotlight_license.column_limit is not None:
        if len(columns) > spotlight_license.column_limit:
            max_columns_hit = True
            columns = columns[: spotlight_license.column_limit]

    columns.extend(table.get_internal_columns())

    max_rows_hit = False
    row_count = len(table)
    if spotlight_license.row_limit is not None:
        if len(table) > spotlight_license.row_limit:
            max_rows_hit = True
            row_count = spotlight_license.row_limit
            for column in columns:
                column.values = column.values[: spotlight_license.row_limit]
                if column.references is not None:
                    column.references = column.references[: spotlight_license.row_limit]

    columns.append(idx_column(row_count))
    if not any(column.name == "__last_edited_at__" for column in columns):
        columns.append(last_edited_at_column(row_count, datetime.now()))
    if not any(column.name == "__last_edited_by__" for column in columns):
        columns.append(last_edited_by_column(row_count, username))

    return ORJSONResponse(
        Table(
            uid=table.get_uid(),
            filename=table.get_name(),
            columns=[Column.from_dataset_column(column) for column in columns],
            max_rows_hit=max_rows_hit,
            max_columns_hit=max_columns_hit,
            generation_id=table.get_generation_id(),
        ).dict()
    )


@router.get(
    "/{column}/{row}",
    tags=["table"],
    operation_id="get_cell",
)
async def get_table_cell(
    column: str, row: int, generation_id: int, request: Request
) -> Any:
    """
    table cell api endpoint
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    cell_data = table.get_cell_data(column, row)
    value = sanitize_values(cell_data)

    if isinstance(value, (bytes, str)):
        return Response(value, media_type="application/octet-stream")

    return value


@router.get(
    "/{column}/{row}/waveform",
    response_model=Optional[List[float]],
    tags=["table"],
    operation_id="get_waveform",
)
async def get_waveform(
    column: str, row: int, generation_id: int, request: Request
) -> Optional[List[float]]:
    """
    table cell api endpoint
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    waveform = table.get_waveform(column, row)

    return sanitize_values(waveform)


class Cells(BaseModel):
    """
    Multiple Cells with the same value
    """

    column: str
    rows: List[int]
    value: Any


# pylint: disable=too-few-public-methods
class CellsUpdateResponse(Cells):
    """
    A cell update (cell + edit information)
    """

    author: str
    edited_at: Optional[datetime]
    generation_id: int


class CellsUpdateRequest(BaseModel):
    """
    Table Cell update request model
    """

    rows: List[int]
    value: Any


class AddColumnRequest(BaseModel):
    """
    Add Column request model
    """

    dtype: str


class MutationResponse(BaseModel):
    """
    Common response model for all mutational endpoints.
    """

    generation_id: int


class AddColumnResponse(MutationResponse):
    """
    Add column response model.
    """

    column: Column


class DuplicateRowResponse(MutationResponse):
    """
    Duplicate row response model.
    """

    row: int


@router.put(
    "/{column}",
    response_model=CellsUpdateResponse,
    tags=["table"],
    operation_id="put_cells",
)
async def put_table_cells(
    column: str,
    generation_id: int,
    update_request: CellsUpdateRequest,
    request: Request,
) -> CellsUpdateResponse:
    """
    replace multiple cell's data

    :raises NoColumnFound: if the column was not found in the dataset
    :raises NoRowFound: if one of the rows was not found in the dataset
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    cells_update = table.replace_cells(
        column, update_request.rows, update_request.value
    )

    return CellsUpdateResponse(
        column=column,
        rows=update_request.rows,
        value=sanitize_values(cells_update.value),
        author=sanitize_values(cells_update.author),
        edited_at=sanitize_values(cells_update.edited_at),
        generation_id=table.get_generation_id(),
    )


@router.delete(
    "/{column}",
    response_model=MutationResponse,
    tags=["table"],
    operation_id="delete_column",
)
async def delete_column(
    column: str, generation_id: int, request: Request
) -> MutationResponse:
    """
    remove a column from the datasets

    :raises NoColumnFound: if a column with the name does not exist
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    table.delete_column(column)

    return MutationResponse(generation_id=table.get_generation_id())


@router.post(
    "/{column}",
    response_model=AddColumnResponse,
    tags=["table"],
    operation_id="add_column",
)
async def add_column(
    column: str,
    generation_id: int,
    add_column_request: AddColumnRequest,
    request: Request,
) -> AddColumnResponse:
    """
    add an editable column

    :raises ColumnExistsError: if a column with the same name exists in the dataset
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    new_column = table.append_column(column, add_column_request.dtype)

    spotlight_license: LicensedFeature = request.app.spotlight_license

    if (
        spotlight_license.row_limit is not None
        and len(table) > spotlight_license.row_limit
    ):
        new_column.values = new_column.values[: spotlight_license.row_limit]
        if new_column.references is not None:
            new_column.references = new_column.references[: spotlight_license.row_limit]

    return AddColumnResponse(
        generation_id=table.get_generation_id(),
        column=Column.from_dataset_column(new_column),
    )


@router.delete(
    "/rows/{row}",
    response_model=MutationResponse,
    tags=["table"],
    operation_id="delete_row",
)
async def delete_row(
    row: int, generation_id: int, request: Request
) -> MutationResponse:
    """
    remove a row from the datasets

    :raises NoRowFound: if a row is not found
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    table.delete_row(row)

    return MutationResponse(generation_id=table.get_generation_id())


@router.post(
    "/rows/{row}",
    response_model=DuplicateRowResponse,
    tags=["table"],
    operation_id="create_row",
)
async def insert_row(
    row: int, generation_id: int, request: Request
) -> DuplicateRowResponse:
    """
    create a new row in the dataset by duplicating a given row

    :raises NoRowFound: if a row is not found
    """
    table: DataSource = request.app.data_source
    table.check_generation_id(generation_id)

    row_index = table.duplicate_row(row)

    return DuplicateRowResponse(generation_id=table.get_generation_id(), row=row_index)


def is_path_relative_to(path: PathType, parent: PathType) -> bool:
    """
    Is the path a subpath of the parent
    """
    try:
        Path(path).relative_to(parent)
        return True
    except ValueError:
        return False


@router.post("/open/{path:path}", tags=["table"], operation_id="open")
async def open_table(path: str, request: Request) -> None:
    """
    Open the specified table file

    :raises InvalidPath: if the supplied path is outside the project root
                         or points to an incompatible file
    """
    full_path = Path(request.app.project_root) / path

    # assert that the path is inside our project root
    if not is_path_relative_to(full_path, request.app.project_root):
        raise InvalidPath(path)

    request.app.data_source = create_datasource(full_path, dtype=None)
