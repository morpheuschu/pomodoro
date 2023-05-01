#!/usr/bin/python3
# python*
# coding = utf-8

import tkinter as tk
from tkinter import messagebox


class Pomodoro(object):

    def __init__(self, study_time, break_time):
        self.study_time = study_time
        self.break_time = break_time

    def get_after_time(self):
        self.study_time = self.study_time * 60 * 1000
        self.break_time = self.break_time * 60 * 1000
        return self.study_time, self.break_time


def show_study_message(break_time):
    ans = messagebox.askquestion("message", f"study times up, breaking?")
    if ans == "yes":
        root.after(break_time, show_break_message)
        lbl_set_time["text"] = f"POMODORO technique part{status} breaking."


def show_break_message():
    global status
    messagebox.showinfo("message", f"break times up")
    btn_start["state"] = "normal"
    lbl_set_time["text"] = f"POMODORO technique part{status} End."
    if status == 4:
        lbl_set_time["text"] = f"end of POMODORO TECHNIQUE"
        status = 0


def go():
    global status
    x = scale.get()
    y = 30 - x
    a = Pomodoro(x, y)
    study_time, break_time = a.get_after_time()
    root.after(study_time, lambda: show_study_message(break_time))
    btn_start["state"] = "disable"
    status = status + 1
    lbl_set_time["text"] = f"POMODORO technique part{status} studying."


root = tk.Tk()
root.title("Pomodoro technique")
root.geometry("400x200-0-0")
status = 0
lbl_set_time = tk.Label(root, text="set pomodoro technique time")
lbl_set_time.pack()
scale = tk.Scale(root, from_=0, to=30, orient=tk.HORIZONTAL)
scale.set(25)
scale.pack()
btn_start = tk.Button(root, text="Start", state="normal", command=go)
btn_start.pack()
root.mainloop()

if __name__ == '__main__':
    pass
