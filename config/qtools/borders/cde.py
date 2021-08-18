"""
This is the 'CDE' border style.
"""


import functools
import xcffib


def cde(self, colors, borderwidth, width, height):
    """
    The "CDE" style is based on the window decorations used by the Common Desktop
    Environment, and has a 3D bevelled look.

    It accepts one border width and three colours. The colours should be in ascending
    brightness to correspond to shadow, normal, and illuminated.

      ______________
     |  _|______|_  |
     |_|          |_|
     | |          | |
     | |          | |
     |_|          |_|
     | |__________| |
     |__|________|__|

    """
    if not colors or not borderwidth:
        return

    if isinstance(colors, str):
        self.set_attribute(borderpixel=self.conn.color_pixel(colors))
        return

    if len(colors) < 3:
        self.set_attribute(borderpixel=self.conn.color_pixel(colors[0]))
        return

    colors = [self.conn.color_pixel(c) for c in colors]
    core = self.conn.conn.core
    outer_w = width + borderwidth * 2
    outer_h = height + borderwidth * 2
    pixmap = self.conn.conn.generate_id()
    gc = self.conn.conn.generate_id()

    try:
        core.CreatePixmap(
            self.conn.default_screen.root_depth, pixmap, self.wid, outer_w, outer_h
        )
        core.CreateGC(gc, pixmap, xcffib.xproto.GC.Foreground, [colors[2]])
        rect = xcffib.xproto.RECTANGLE.synthetic(0, 0, outer_w, outer_h)
        core.PolyFillRectangle(pixmap, gc, 1, [rect])

        core.ChangeGC(gc, xcffib.xproto.GC.Foreground, [colors[1]])
        rect = xcffib.xproto.RECTANGLE.synthetic(2, 2, outer_w - 4, outer_h - 4)
        core.PolyFillRectangle(pixmap, gc, 1, [rect])

        core.ChangeGC(gc, xcffib.xproto.GC.Foreground, [colors[0]])
        rect = xcffib.xproto.RECTANGLE.synthetic(
            borderwidth - 1, borderwidth - 1, width + 2, height + 2
        )
        core.PolyFillRectangle(pixmap, gc, 1, [rect])

        shadows, light = _lines(borderwidth, outer_w, outer_h)
        core.PolyLine(0, pixmap, gc, 18, shadows)
        core.ChangeGC(gc, xcffib.xproto.GC.Foreground, [colors[2]])
        core.PolyLine(0, pixmap, gc, 15, light)
        self.set_borderpixmap(pixmap, gc, borderwidth, width, height)

    finally:
        core.FreePixmap(pixmap)
        core.FreeGC(gc)


@functools.lru_cache()
def _lines(borderwidth, outer_w, outer_h):
    shadows = [
        xcffib.xproto.POINT.synthetic(1, outer_h - 1),
        xcffib.xproto.POINT.synthetic(outer_w, outer_h - 1),
        xcffib.xproto.POINT.synthetic(outer_w - 1, outer_h - 1),
        xcffib.xproto.POINT.synthetic(outer_w - 1, 1),
        xcffib.xproto.POINT.synthetic(outer_w - 1, 2),
        xcffib.xproto.POINT.synthetic(outer_w - 2, 2),
        xcffib.xproto.POINT.synthetic(outer_w - 2, outer_h - 1),
        xcffib.xproto.POINT.synthetic(outer_w - 2, outer_h - 2),
        xcffib.xproto.POINT.synthetic(2, outer_h - 2),
        xcffib.xproto.POINT.synthetic(borderwidth + 19, outer_h - 2),
        xcffib.xproto.POINT.synthetic(borderwidth + 19, 1),
        xcffib.xproto.POINT.synthetic(borderwidth + 19, borderwidth + 19),
        xcffib.xproto.POINT.synthetic(1, borderwidth + 19),
        xcffib.xproto.POINT.synthetic(outer_w, borderwidth + 19),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 21, borderwidth + 19),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 21, 1),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 21, outer_h),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 21, outer_h - borderwidth - 21),
        xcffib.xproto.POINT.synthetic(outer_w, outer_h - borderwidth - 21),
        xcffib.xproto.POINT.synthetic(1, outer_h - borderwidth - 21),
    ]
    light = [
        xcffib.xproto.POINT.synthetic(borderwidth + 20, outer_h - 1),
        xcffib.xproto.POINT.synthetic(borderwidth + 20, 1),
        xcffib.xproto.POINT.synthetic(borderwidth + 20, borderwidth + 20),
        xcffib.xproto.POINT.synthetic(1, borderwidth + 20),
        xcffib.xproto.POINT.synthetic(outer_w - 1, borderwidth + 20),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 20, borderwidth + 20),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 20, 1),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 20, outer_h - 1),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth - 20, outer_h - borderwidth - 20),
        xcffib.xproto.POINT.synthetic(outer_w - 1, outer_h - borderwidth - 20),
        xcffib.xproto.POINT.synthetic(1, outer_h - borderwidth - 20),
        xcffib.xproto.POINT.synthetic(borderwidth, outer_h - borderwidth - 20),
        xcffib.xproto.POINT.synthetic(borderwidth, outer_h - borderwidth),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth + 1, outer_h - borderwidth),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth, outer_h - borderwidth),
        xcffib.xproto.POINT.synthetic(outer_w - borderwidth, borderwidth),
    ]
    return shadows, light
