from dataclasses import dataclass
from typing import Union
from overrides import override
from ..internals.buildable import Buildable
from ..internals.build_context import BuildContext
from .fill import Fill
from .text_style import TextStyle
from .border import Border
from .style import Style


@dataclass(frozen=True)
class Styler(Buildable):
    child: Buildable
    fill: Union[Fill, None] = None
    text_style: Union[TextStyle, None] = None
    parent_border: Union[Border, None] = None
    child_border: Union[Border, None] = None

    @override
    def internal_build(self, context: BuildContext) -> None:
        new_context = context.with_style_change(
            self.style, self.child.get_size())
        self.child.internal_build(new_context)

    @override
    def build(self) -> 'Buildable':
        return self.child

    @property
    def style(self):
        return Style(
            fill=self.fill,
            text_style=self.text_style,
            parent_border=self.parent_border,
            child_border=self.child_border
        )

    @staticmethod
    def from_style(child: Buildable, style: Style):
        return Styler(child, style.fill, style.text_style, style.parent_border, style.child_border)
