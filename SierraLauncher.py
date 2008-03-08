#!/usr/bin/env python

# Sierra Launcher replacement by C C Magnus Gustavsson

import os, pygtk
pygtk.require('2.0')

from gtk import *

# Actions for Linux/Unix (instead of SierraLauncher.ini)
actions = ["acroread Manuals/KQManual.pdf &",
           "dosbox kq1sci/SIERRA.COM -fullscreen -exit &",
           "dosbox kq2/SIERRA.COM -fullscreen -exit &",
           "dosbox kq3/SIERRA.COM -fullscreen -exit &",
           "dosbox kq4/SIERRA.COM -fullscreen -exit &",
           "dosbox kq5/SIERRA.EXE -fullscreen -exit &",
           "dosbox kq6/SIERRA.EXE -fullscreen -exit &",
           "wine kq7/SIERRAW.EXE kq7/RESOURCE.WIN &"]

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
        self.window.set_title("King's Quest Collection(TM)")
        self.window.set_icon_from_file("Sierra.ico")
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.table = Table(columns=3, rows=9, homogeneous=False)
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
            self.table.attach(self.frame, 0, 2, i-1, i, xoptions=FILL,
                              yoptions=FILL, xpadding=8, ypadding=2)
            self.frame.show()

        self.button = Button('View Manual')
        self.button.num = 0
        self.button.connect("clicked", self.launch, None)
        self.table.attach(self.button, 0, 1, 7, 8, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = Button('     Close     ')
        self.button.connect_object("clicked", Widget.destroy, self.window)
        self.table.attach(self.button, 1, 2, 7, 8, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.button = CheckButton("Close window on launch")
        self.button.set_active(self.close_window_on_launch)
        self.button.connect("toggled", self.toggle, None)
        self.table.attach(self.button, 0, 2, 8, 9, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=4, ypadding=4)
        self.button.show()

        self.image = Image()
        self.image.set_from_file("gameart.bmp")
        self.table.attach(self.image, 2, 3, 0, 9, xoptions=EXPAND,
                          yoptions=EXPAND, xpadding=8, ypadding=8)
        self.image.show()

        self.table.show()
        self.window.show()

    def main(self):
        main()

if __name__ == "__main__":
    SierraLauncher().main()
