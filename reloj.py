import tkinter as tk
import time

ROOT = tk.Tk()
ROOT.geometry("200x100")
lblReloj = tk.Label(ROOT, text="00:00")
lblReloj.pack()


def reloj():
    global hora
    hora = time.strftime("%H:%M")
    lblReloj.config(text=hora)
    lblReloj.after(1000, reloj)


reloj()

ROOT.mainloop()
