import tkinter as tk
import time

ROOT = tk.Tk()
ROOT.geometry("300x100")
ROOT.title("Hora actual")
ROOT.configure(bg="Black")
lblReloj = tk.Label(ROOT, text="00:00", fg="green",
                    bg="black", font=("", 70))
lblReloj.pack()


def reloj():
    global hora
    hora = time.strftime("%H:%M")
    lblReloj.config(text=hora)
    lblReloj.after(1000, reloj)


reloj()

ROOT.mainloop()
