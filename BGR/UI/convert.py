import tkinter as tk
import state
root = tk.Tk()
root.geometry(f"{400}x{400}")
root.title("convertor")
root.configure(bg="#FFFFFF")
root.resizable(False, False)
title_label = tk.Label(root, text="IMG-convertor", font=state.TITLE_FONT, bg=state.WINDOW_BACKGROUND_COLOR)
title_label.pack(padx=20, pady=10)

canvas = tk.Canvas(root, width=400 , height=400, bg="white")
canvas.pack()
root.mainloop()