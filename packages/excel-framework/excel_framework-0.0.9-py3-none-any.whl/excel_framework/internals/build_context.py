from abc import ABC
from typing import Union
from dataclasses import dataclass
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from ..sizes.resizer import Resizer
from ..sizes.dimension import Dimension, ColumnDimension
from ..sizes.size import Size
from ..styling.border import ParentBorderCoordinates
from ..styling.style import Style


@dataclass
class BuildContext(ABC):
    workbook: Workbook
    sheet: Worksheet
    resizer: Resizer
    row_index: int = 1
    column_index: int = 1
    style: Union[Style, None] = None
    parent_border_coordinates: Union[ParentBorderCoordinates, None] = None

    @staticmethod
    def initial(title: str, dimensions: list[Dimension]) -> 'BuildContext':
        workbook = Workbook()
        workbook.active.title = title
        return BuildContext(workbook, workbook.active, Resizer(workbook.active, dimensions))

    def new_sheet(self, title: str, dimensions: list[Dimension]) -> 'BuildContext':
        new_sheet: Worksheet = self.workbook.create_sheet(title)
        return BuildContext(self.workbook, new_sheet, Resizer(new_sheet, dimensions))

    def collect_length(self, length: int):
        self.resizer.collect_length(self.row_index, self.column_index, length)

    def collect_column_dimension(self, dimension: ColumnDimension):
        self.resizer.collect_column_dimension(dimension)

    def with_style_change(self, new_style: Style, child_size: Size) -> 'BuildContext':
        if self.style:
            new_style = self.style.join(new_style)
        new_parent_border_coordinates = self.parent_border_coordinates
        if new_style.parent_border:
            new_parent_border_coordinates = ParentBorderCoordinates(
                self.row_index,
                self.column_index,
                self.row_index + child_size.height - 1,
                self.column_index + child_size.width - 1
            )
        return BuildContext(
            self.workbook,
            self.sheet,
            self.resizer,
            self.row_index,
            self.column_index,
            new_style,
            new_parent_border_coordinates
        )
