import sys
from pathlib import Path
sys.path.append(str(Path.home()) + "/.config/polybar/scripts/")
from conf import Filesystem_Settings as conf
from utils import Utils
from tkinter import *
import subprocess


######Даже не пытайся прочесть сей говнокод######

#Подкапотные настройки (не трогать!!!)
spawn_x, spawn_y = Utils.get_spawn_coordinates(conf.window_w)


class Filesystem_GUI():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("filesystem")
        self.tk.geometry(f"{conf.window_w}x{str(len(conf.directories)*35+35)}+{spawn_x}+{spawn_y}")
        self.tk.resizable(False, False)
        def open_dir(directory):
            subprocess.Popen([conf.file_manager, directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.tk.destroy()
        def quit():
            self.tk.destroy()
        Button(self.tk, text="Quit x", font=conf.font_btn_text, command=quit).place(x=0, height=35, width=conf.window_w, y=0)
        for i in range(len(conf.directories)):
            Button(self.tk, text=conf.directories[i], font=conf.font_btn_text, command=lambda directory=conf.directories[i]: open_dir(directory=directory)).place(x=0, height=35, width=conf.window_w, y=(i*35+35))
        self.tk.mainloop()



GUI = Filesystem_GUI()