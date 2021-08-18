from libqtile.config import Screen
from ..bar import bottom_bar, top_bar

screens = [
    Screen(
        bottom=bottom_bar,
        top=top_bar,
        )
]
