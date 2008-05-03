#!/usr/bin/env python

# Sierra Launcher replacement by C C Magnus Gustavsson

import os, pygtk
pygtk.require('2.0')

from gtk import *

# Actions for Linux/Unix (instead of SierraLauncher.ini)
actions = ["acroread kq/Manuals/KQManual.pdf &",
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
           "dosbox lsl/lsl6/SIERRA.EXE -fullscreen -exit &"]

class SierraLauncher:
    def destroy(self, widget, data=None):
        main_quit()

    def delete_event(self, widget, event, data=None):
        self.destroy(self, widget)

    def launch(self, widget, data=None):
        os.system(actions[widget.num])
        if self.close_window_on_launch:
            self.destroy(self, widget)

    def toggle(self, widget, data=None):
        self.close_window_on_launch = widget.get_active()

    def __init__(self):
        self.close_window_on_launch = False

        self.window = Window(WINDOW_TOPLEVEL)
        self.window.set_title("Sierra Collections")
        self.window.set_icon_from_file("kq/Sierra.ico")
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.table = Table(columns=5, rows=9, homogeneous=False)
        self.table.set_border_width(8)
        self.window.add(self.table)

        for i in range(1, 8):
            self.button = Button('               Launch               ')
            self.button.num = i
            self.button.connect("clicked", self.launch, None)
            self.button.set_border_width(4)
            self.button.show()

            self.frame = Frame("King's Quest " + str(i))
            self.frame.add(self.button)
            self.table.attach(self.frame, 0, 1, i-1, i, xoptions=FILL,
                              yoptions=FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.button = Button('View Manual')
        self.button.num = 0
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 0, 1, 7, 8, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=16)
        self.button.show()

        for i in range(1, 6):
            self.button = Button('               Launch               ')
            self.button.num = i+8
            self.button.connect("clicked", self.launch, None)
            self.button.set_border_width(4)
            self.button.show()

            if i > 3:
                self.frame = Frame("Leisure Suit Larry " + str(i+1))
            else:
                self.frame = Frame("Leisure Suit Larry " + str(i))
            self.frame.add(self.button)
            self.table.attach(self.frame, 4, 5, i-1, i, xoptions=FILL,
                              yoptions=FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.button = Button('View Manual')
        self.button.num = 8
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 4, 5, 5, 6, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Button('     Close     ')
        self.button.connect_object("clicked", Widget.destroy, self.window)
        self.table.attach(self.button, 4, 5, 7, 8, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = CheckButton("Close window on launch")
        self.button.set_active(self.close_window_on_launch)
        self.button.connect("toggled", self.toggle, None)
        self.table.attach(self.button, 4, 5, 8, 9, xoptions=EXPAND,
                          yoptions=0, xpadding=4, ypadding=4)
        self.button.show()

        self.image = Image()
        pixbuf = gdk.pixbuf_new_from_file("kq/gameart.bmp")
        scaled_buf = pixbuf.scale_simple(200, 237, gdk.INTERP_BILINEAR)
        self.image.set_from_pixbuf(scaled_buf)
        self.table.attach(self.image, 2, 3, 0, 4, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=8, ypadding=4)
        self.image.show()

        self.image = Image()
        pixbuf = gdk.pixbuf_new_from_file("lsl/gameart.bmp")
        scaled_buf = pixbuf.scale_simple(200, 237, gdk.INTERP_BILINEAR)
        self.image.set_from_pixbuf(scaled_buf)
        self.table.attach(self.image, 2, 3, 4, 9, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=8, ypadding=2)
        self.image.show()

        self.arrow = Arrow(ARROW_LEFT, SHADOW_OUT)
        self.table.attach(self.arrow, 1, 2, 0, 1, xoptions=SHRINK,
                          yoptions=SHRINK, xpadding=2, ypadding=2)
        self.arrow.show()

        self.arrow = Arrow(ARROW_RIGHT, SHADOW_OUT)
        self.table.attach(self.arrow, 3, 4, 4, 5, xoptions=SHRINK,
                          yoptions=SHRINK, xpadding=2, ypadding=2)
        self.arrow.show()

        self.table.show()
        self.window.show()

    def main(self):
        main()

if __name__ == "__main__":
    SierraLauncher().main()
