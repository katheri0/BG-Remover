import tkinter as tk
from UI.layout import build_layout
from UI.state import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_BACKGROUND_COLOR

def main():
    root = tk.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.title("BG-Remover")
    root.configure(bg=WINDOW_BACKGROUND_COLOR)
    root.resizable(False, False)

    # Initialize UI
    build_layout(root)

    root.mainloop()

if __name__ == "__main__":
    main()