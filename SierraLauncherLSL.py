#!/usr/bin/env python3

'''Sierra Launcher replacement by C C Magnus Gustavsson'''

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.Gtk import AttachOptions as options

# Actions for Linux/Unix (instead of SierraLauncher.ini)
ACTIONS = [
    "acroread Manuals/LarryManual.pdf &",
    "dosbox lsl1vga/SCIDHUV.EXE -fullscreen -exit &",
    "dosbox lsl2/SIERRA.COM -fullscreen -exit &",
    "dosbox lsl3/SIERRA.COM -fullscreen -exit &",
    "gedit lsl4/README.TXT &",
    "dosbox lsl5/SCIDHUV.EXE -fullscreen -exit &",
    "dosbox lsl6/SIERRA.EXE -fullscreen -exit &"
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
        self.window.set_title("Leisure Suit Larry Collection(TM)")
        self.window.set_icon_from_file("Sierra.ico")
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.table = Gtk.Table(columns=3, rows=9, homogeneous=False)
        self.table.set_border_width(8)
        self.window.add(self.table)

        for i in range(1, 7):
            self.button = Gtk.Button('{:^36}'.format('Launch'))
            self.button.num = i
            self.button.connect("clicked", self.launch, None)
            self.button.set_border_width(4)
            self.button.show()

            self.frame = Gtk.Frame(label="Leisure Suit Larry {:d}".format(i))
            self.frame.add(self.button)
            self.table.attach(self.frame, 0, 2, i-1, i, xoptions=options.FILL,
                              yoptions=options.FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.dummy = Gtk.Frame()
        self.table.attach(self.dummy, 0, 2, 6, 7, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=8, ypadding=2)

        self.button = Gtk.Button('View Manual')
        self.button.num = 0
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 0, 1, 7, 8, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Gtk.Button('{:^15}'.format('Close'))
        self.button.connect_object("clicked", Gtk.Widget.destroy, self.window)
        self.table.attach(self.button, 1, 2, 7, 8, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Gtk.CheckButton("Close window on launch")
        self.button.set_active(self.close_window_on_launch)
        self.button.connect("toggled", self.toggle, None)
        self.table.attach(self.button, 0, 2, 8, 9, xoptions=options.EXPAND,
                          yoptions=0, xpadding=4, ypadding=4)
        self.button.show()

        self.image = Gtk.Image()
        self.image.set_from_file("gameart.bmp")
        self.table.attach(self.image, 2, 3, 0, 9, xoptions=options.EXPAND,
                          yoptions=options.EXPAND, xpadding=8, ypadding=8)
        self.image.show()

        self.table.show()
        self.window.show()

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    SierraLauncher().main()
