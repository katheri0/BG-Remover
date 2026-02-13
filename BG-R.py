import tkinter as tk
# from rembg import remove
# from PIL import Image

root = tk.Tk()
root.geometry("720x512")
root.title("BG-Remover")

label = tk.Label(root, text="BG-Remover", font=("Arial", 27))
label.pack(padx=20, pady=10)

canvas = tk.Canvas(root, width=700, height=450, bg="white")
canvas.pack()


def create_rounded_rectangle(canvas, left_x, top_y, right_x, bottom_y, corner_radius=25, **options):
    points = [
        left_x + corner_radius, top_y,
        right_x - corner_radius, top_y,
        right_x, top_y,
        right_x, top_y + corner_radius,
        right_x, bottom_y - corner_radius,
        right_x, bottom_y,
        right_x - corner_radius, bottom_y,
        left_x + corner_radius, bottom_y,
        left_x, bottom_y,
        left_x, bottom_y - corner_radius,
        left_x, top_y + corner_radius,
        left_x, top_y
    ]

    return canvas.create_polygon(points, smooth=True, **options)


# Left rectangle
create_rounded_rectangle(
    canvas,
    left_x=50,
    top_y=100,
    right_x=300,
    bottom_y=300,
    corner_radius=40,
    fill="#FFF0CF",
    outline="black",
    width=2,
    dash=(10, 2)
)

create_rounded_rectangle(
    canvas,
    left_x=400,
    top_y=100,
    right_x=650,
    bottom_y=300,
    corner_radius=40,
    fill="#FFF0CF",
    outline="black",
    width=2,
    dash=(10, 2)

)


root.mainloop()
