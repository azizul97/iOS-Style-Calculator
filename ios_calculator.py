import tkinter as tk
from tkinter import messagebox
import math

def on_click(button_text):
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "log":
        try:
            value = float(entry.get())
            result = math.log10(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for log calculation")
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("ios style calculator")
root.geometry("350x500")
root.configure(bg="#1C1C1E")

entry = tk.Entry(root, font=("Helvetica", 24), bg="#2C2C2E", fg="white", bd=0, justify=tk.RIGHT)
entry.pack(pady=20, padx=10, ipadx=8, ipady=8, fill=tk.BOTH)

buttons = [
    ("CE", "log", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", "00", ".", "=")
]

button_bg = {"C": "#FF3B30", "log": "#FF9500", "=": "#34C759", "/": "#FF9500", "*": "#FF9500", "-": "#FF9500", "+": "#FF9500"}

frame = tk.Frame(root, bg="#1C1C1E")
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame, bg="#1C1C1E")
    button_row.pack(expand=True, fill="both")
    for btn_text in row:
        btn_color = button_bg.get(btn_text, "#505050")
        btn = tk.Button(
            button_row, text=btn_text, font=("Helvetica", 20), fg="white", bg=btn_color,
            relief=tk.FLAT, width=5, height=2, command=lambda x=btn_text: on_click(x)
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()
