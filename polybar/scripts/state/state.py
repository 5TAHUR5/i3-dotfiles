import sys
from pathlib import Path
sys.path.append(str(Path.home()) + "/.config/polybar/scripts/")
from conf import State_Settings as conf
from utils import Utils
from tkinter import *
from tkinter import messagebox as mb
import threading, time, subprocess



######Даже не пытайся прочесть сей говнокод######

#Подкапотные настройки (не трогать!!!)
label = sys.argv[1]
spawn_x, spawn_y = Utils.get_spawn_coordinates(conf.window_w)
get_pids_script = str(Path.home()) + f"/.config/polybar/scripts/state/{label}.sh"


class State_GUI():
    def __init__(self):
        self.running = True
        self.tk = Tk()
        self.tk.title(label)
        self.tk.geometry(f"{conf.window_w}x{str(conf.count_pid*35+25)}+{spawn_x}+{spawn_y}")
        self.tk.resizable(False, False)
        ##def focus_out(event):
        ##    if destroy_if_focus_out:
        ##        self.tk.destroy()
        ##self.tk.bind("<FocusOut>", focus_out)
        Frame(borderwidth=1, relief=SOLID, name="frame_sign").place(x=0, y=0, height=25, width=conf.window_w)
        def quit():
            self.tk.destroy()
        Button(self.tk.nametowidget("frame_sign"), text="q", font=conf.font_for_lbl, command=quit).place(width=25, height=21, x=int(conf.window_w)-30, y=2)
        Label(self.tk.nametowidget("frame_sign"), text=conf.sigh_label_text(sys.argv[1]), font=conf.font_for_lbl).place(x=10, y=0)
        for i in range(conf.count_pid):
            pid_frame = Frame(self.tk, borderwidth=1, relief=SOLID, name=("pid_fr" + str(i)))
            Label(pid_frame, text=i, font=conf.font_for_lbl, name=("pid_lbl" + str(i))).place(x=7, y=5)
            Label(pid_frame, text=i, font=conf.font_for_lbl, name=("index_lbl" + str(i))).place(x=55, y=5)
            Label(pid_frame, text=i, font=conf.font_for_lbl, name=("comm_lbl" + str(i))).place(x=100, y=5)
            Button(pid_frame, text="x", bg='red', font=conf.font_for_lbl, name=("kill_btn" + str(i))).place(x=220, y=5, height=25, width=25)
            pid_frame.place(x=0, y=(i*35+25), height=35, width=conf.window_w)
    def auto_update(self):
        while self.running:
            pids_str = subprocess.Popen(["bash", get_pids_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()[0].split("\n")
            def kill_pid(pid, comm):
                if mb.askyesno(title="Kill pig?",message=(f"Kill pid {pid} with command {comm}?")):
                    subprocess.Popen(["kill", pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for i in range(conf.count_pid):
                pid_strs = pids_str[i].split("|")
                self.tk.nametowidget(f"pid_fr{i}.pid_lbl{i}").config(text=pid_strs[0])
                self.tk.nametowidget(f"pid_fr{i}.index_lbl{i}").config(text=pid_strs[1])
                self.tk.nametowidget(f"pid_fr{i}.comm_lbl{i}").config(text=pid_strs[2])
                self.tk.nametowidget(f"pid_fr{i}.kill_btn{i}").config(command=lambda pid=pid_strs[0], comm=pid_strs[2]: kill_pid(pid=pid, comm=comm))
            time.sleep(conf.second_for_update)
        self.tk.destroy()
    def run(self):
        self.thread = threading.Thread(target=self.auto_update)
        self.thread.start()
        self.tk.mainloop()

GUI = State_GUI()
GUI.run()