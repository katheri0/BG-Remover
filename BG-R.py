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

# Right rectangle
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

# btn rectangle
create_rounded_rectangle(
    canvas,
    left_x=270,
    top_y=350,
    right_x=430,
    bottom_y=400,
    corner_radius=40,
    fill="#FFF0CF",
    outline="black",
    width=2,
    dash=(10, 2)

)


canvas.create_text(
    175, 200,
    text="Original Image",
    font=("Arial", 16),
    fill="black"
)


canvas.create_text(
    525, 200,
    text="Result",
    font=("Arial", 16),
    fill="black"
)

canvas.create_text(
    353, 375,
    text="Result",
    font=("Arial", 16),
    fill="black"
)

canvas.create_text(
    215, 430,
    text="developed by Katheri Saleh using ",
    font=("Arial", 16),
    fill="black"
)

canvas.create_text(
    30, 430,
    text="</>",
    font=("Arial", 25),
    fill="black"
)
# developed by Katheri Saleh using

canvas.create_text(
    500, 430,
    text="Contacts: 778484033",
    font=("Arial", 16),
    fill="black"
)
# Contacts: 778484033
canvas.create_text(
    660, 430,
    text=" GH: Katheri0",
    font=("Arial", 14),
    fill="black"
)

# Katheri0
root.mainloop()
