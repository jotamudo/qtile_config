from libqtile.lazy import lazy
from libqtile.config import Key

backlight_keys = [
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"))
        ]
