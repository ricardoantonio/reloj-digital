import tkinter as tk
import time
import locale

try:
    locale.setlocale(locale.LC_ALL, "esp")
except:
    locale.setlocale(locale.LC_ALL, "es_ES")

ROOT = tk.Tk()
ROOT.geometry("300x100")
ROOT.title("Hora actual")
ROOT.configure(bg="Black")

fecha = time.strftime("%A, %d de %B de %Y")
lblFecha = tk.Label(ROOT, text=fecha, fg="green", bg="black")
lblFecha.pack()
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
