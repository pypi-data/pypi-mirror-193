from ...internals.buildable import Buildable
from overrides import override
from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, Any, Union
from .column import Column
from .row import Row
from ..non_layout.excel_cell import ExcelCell
from ...styling.style import Style
from ...styling.styler import Styler
from ...internals.build_context import BuildContext
from ...sizes.dimension import ColumnDimension, AutoWidth, FixedWidth

T = TypeVar("T")


@dataclass(frozen=True)
class TableColumn(Generic[T]):
    name: str
    value: Callable[[T], Any]
    width: Union[AutoWidth, FixedWidth, None] = None
    column_name_style: Union[Style, None] = None
    value_style: Union[Callable[[T], Style], None] = None


@dataclass(frozen=True)
class Table(Buildable, Generic[T]):
    columns: list[TableColumn[T]]
    data: list[T]
    column_name_style: Union[Style, None] = None
    data_style: Union[Style, None] = None

    @override
    def internal_build(self, context: BuildContext) -> None:
        for i, column in enumerate(self.columns):
            if column.width:
                context.collect_column_dimension(
                    ColumnDimension(context.column_index + i, column.width)
                )
        self.build().internal_build(context)

    @override
    def build(self, ) -> 'Buildable':
        return Column([
            Styler.from_style(
                Row(children=self.__get_column_name_cells()),
                self.column_name_style if self.column_name_style else Style()
            ),
            Styler.from_style(
                Column(children=self.__get_value_rows()),
                self.data_style if self.data_style is not None else Style()
            )
        ])

    def __get_column_name_cells(self) -> list[Buildable]:
        excel_cells = []
        for column in self.columns:
            excel_cells.append(
                Styler.from_style(
                    ExcelCell(column.name),
                    column.column_name_style if column.column_name_style else Style()
                )
            )
        return excel_cells

    def __get_value_rows(self) -> list[Buildable]:
        rows = []
        for model in self.data:
            excel_cells = []
            for column in self.columns:
                value = column.value(model)
                style = column.value_style(
                    model) if column.value_style else Style()
                excel_cells.append(Styler.from_style(ExcelCell(value), style))
            rows.append(Row(children=excel_cells))
        return rows
