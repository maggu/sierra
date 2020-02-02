#!/usr/bin/env python3

'''Sierra Launcher replacement by C C Magnus Gustavsson'''

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import GdkPixbuf, Gtk
from gi.repository.GdkPixbuf import InterpType as interp_type
from gi.repository.Gtk import AttachOptions as options

# Actions for Linux/Unix (instead of SierraLauncher.ini)
ACTIONS = [
    "acroread kq/Manuals/KQManual.pdf &",
    "dosbox kq/kq1sci/SIERRA.COM -fullscreen -exit &",
    "dosbox kq/kq2/SIERRA.COM -fullscreen -exit &",
    "dosbox kq/kq3/SIERRA.COM -fullscreen -exit &",
    "dosbox kq/kq4/SIERRA.COM -fullscreen -exit &",
    "dosbox kq/kq5/SIERRA.EXE -fullscreen -exit &",
    "dosbox kq/kq6/SIERRA.EXE -fullscreen -exit &",
    "wine kq/kq7/SIERRAW.EXE kq/kq7/RESOURCE.WIN &",
    "acroread lsl/Manuals/LarryManual.pdf &",
    "dosbox lsl/lsl1vga/SCIDHUV.EXE -fullscreen -exit &",
    "dosbox lsl/lsl2/SIERRA.COM -fullscreen -exit &",
    "dosbox lsl/lsl3/SIERRA.COM -fullscreen -exit &",
    "dosbox lsl/lsl5/SCIDHUV.EXE -fullscreen -exit &",
    "dosbox lsl/lsl6/SIERRA.EXE -fullscreen -exit &"
]

class SierraLauncher(object):
    def destroy(self, widget, data=None):
        Gtk.main_quit()

    def delete_event(self, widget, event, data=None):
        self.destroy(self, widget)

    def launch(self, widget, data=None):
        os.system(ACTIONS[widget.num])
        if self.close_window_on_launch:
            self.destroy(self, widget)

    def toggle(self, widget, data=None):
        self.close_window_on_launch = widget.get_active()

    def __init__(self):
        self.close_window_on_launch = False

        self.window = Gtk.Window()
        self.window.set_title("Sierra Collections")
        self.window.set_icon_from_file("kq/Sierra.ico")
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.table = Gtk.Table(columns=5, rows=9, homogeneous=False)
        self.table.set_border_width(8)
        self.window.add(self.table)

        for i in range(1, 8):
            self.button = Gtk.Button('{:^36}'.format('Launch'))
            self.button.num = i
            self.button.connect("clicked", self.launch, None)
            self.button.set_border_width(4)
            self.button.show()

            self.frame = Gtk.Frame(label="King's Quest {:d}".format(i))
            self.frame.add(self.button)
            self.table.attach(self.frame, 0, 1, i-1, i, xoptions=options.FILL,
                              yoptions=options.FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.button = Gtk.Button('View Manual')
        self.button.num = 0
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 0, 1, 7, 8, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=4, ypadding=16)
        self.button.show()

        for i in range(1, 6):
            self.button = Gtk.Button('{:^36}'.format('Launch'))
            self.button.num = i+8
            self.button.connect("clicked", self.launch, None)
            self.button.set_border_width(4)
            self.button.show()

            v = i + 1 if i > 3 else i
            self.frame = Gtk.Frame(label="Leisure Suit Larry {:d}".format(v))
            self.frame.add(self.button)
            self.table.attach(self.frame, 4, 5, i-1, i, xoptions=options.FILL,
                              yoptions=options.FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.button = Gtk.Button('View Manual')
        self.button.num = 8
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 4, 5, 5, 6, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Gtk.Button('{:^15}'.format('Close'))
        self.button.connect_object("clicked", Gtk.Widget.destroy, self.window)
        self.table.attach(self.button, 4, 5, 7, 8, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Gtk.CheckButton("Close window on launch")
        self.button.set_active(self.close_window_on_launch)
        self.button.connect("toggled", self.toggle, None)
        self.table.attach(self.button, 4, 5, 8, 9, xoptions=options.EXPAND,
                          yoptions=0, xpadding=4, ypadding=4)
        self.button.show()

        self.image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("kq/gameart.bmp")
        scaled_buf = pixbuf.scale_simple(200, 237, interp_type.BILINEAR)
        self.image.set_from_pixbuf(scaled_buf)
        self.table.attach(self.image, 2, 3, 0, 4, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=8, ypadding=4)
        self.image.show()

        self.image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("lsl/gameart.bmp")
        scaled_buf = pixbuf.scale_simple(200, 237, interp_type.BILINEAR)
        self.image.set_from_pixbuf(scaled_buf)
        self.table.attach(self.image, 2, 3, 4, 9, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=8, ypadding=2)
        self.image.show()

        self.arrow = Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.OUT)
        self.table.attach(self.arrow, 1, 2, 0, 1, xoptions=options.SHRINK,
                          yoptions=options.SHRINK, xpadding=2, ypadding=2)
        self.arrow.show()

        self.arrow = Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.OUT)
        self.table.attach(self.arrow, 3, 4, 4, 5, xoptions=options.SHRINK,
                          yoptions=options.SHRINK, xpadding=2, ypadding=2)
        self.arrow.show()

        self.table.show()
        self.window.show()

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    SierraLauncher().main()
