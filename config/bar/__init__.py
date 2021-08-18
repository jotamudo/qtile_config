from libqtile import bar, widget

widget_defaults = dict(
    font='Iosevka Custom',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

bar_background = "#1d2021"

bottom_bar = bar.Bar(
            [
                widget.CurrentLayout(),
                widget.Sep(),
                widget.WindowName(),
                # widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Backlight(),
                widget.Sep(),
                widget.Memory(),
                widget.Sep(),
                widget.Battery(),
                widget.BatteryIcon(),
                widget.Sep(),
                widget.Volume(),
                widget.Sep(),
                widget.Systray(),
                widget.Sep(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
            background=bar_background
        )

top_bar = bar.Bar(
            [
                widget.Spacer(),
                widget.GroupBox(),
                widget.Spacer()
                ],
            24,
            background=bar_background
            )
