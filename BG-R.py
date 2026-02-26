import tkinter as tk
# from rembg import remove
from PIL import Image, ImageTk


# ==========================
# Window Configuration
# ==========================

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 512
WINDOW_BACKGROUND_COLOR = "#FFFFFF"
TITLE_FONT = ("Arial", 27)
DEFAULT_FONT = ("Arial", 14)
REMOVE_BUTTON_DEFAULT_COLOR = "#FFF0CF"
REMOVE_BUTTON_HOVER_COLOR = "#F7D88A"  # slightly darker
UPLOAD__DOWNLOAD_AREA_DEFAULT_COLOR = "#FFF0CF"
UPLOAD__DOWNLOAD_AREA_HOVER_COLOR = "#FDE6A8"
# ==========================
# Helper Functions
# ==========================

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


def load_canvas_image(canvas, image_path, x_position, y_position, width=None, height=None):
    image = Image.open(image_path)

    if width and height:
        image = image.resize((width, height))

    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(x_position, y_position, image=photo_image)

    return photo_image  # prevent garbage collection


# ==========================
# Main Application
# ==========================

root = tk.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.title("BG-Remover")
root.configure(bg=WINDOW_BACKGROUND_COLOR)

title_label = tk.Label(
    root,
    text="BG-Remover",
    font=TITLE_FONT,
    bg=WINDOW_BACKGROUND_COLOR
)
title_label.pack(padx=20, pady=10)

main_canvas = tk.Canvas(
    root,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    bg="white"
)
main_canvas.pack()


# ==========================
# Layout - Rectangles
# ==========================

upload_area_id = create_rounded_rectangle(
    main_canvas,
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
download_area_id = create_rounded_rectangle(
    main_canvas,
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

remove_button_id = create_rounded_rectangle(
    main_canvas,
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


# ==========================
# Text Elements
# ==========================

main_canvas.create_text(175, 260, text="Upload Image", font=("Arial", 16))
main_canvas.create_text(353, 375, text="Remove", font=("Arial", 14))

main_canvas.create_text(
    200, 430,
    text="developed by Katheri Saleh using",
    font=DEFAULT_FONT
)

main_canvas.create_text(30, 430, text="</>", font=("Arial", 25))

main_canvas.create_text(
    505, 430,
    text="Contacts:      778484033",
    font=DEFAULT_FONT
)

main_canvas.create_text(
    680, 430,
    text="Katheri0",
    font=DEFAULT_FONT
)

# ==========================
# Hover Elements
# ==========================

# ****************
# remove button
# ****************

def on_remove_button_enter(event):
    main_canvas.itemconfig(remove_button_id, fill=REMOVE_BUTTON_HOVER_COLOR)
    root.config(cursor="hand2")


def on_remove_button_leave(event):
    main_canvas.itemconfig(remove_button_id, fill=UPLOAD__DOWNLOAD_AREA_DEFAULT_COLOR)
    root.config(cursor="")

main_canvas.tag_bind(remove_button_id, "<Enter>", on_remove_button_enter)
main_canvas.tag_bind(remove_button_id, "<Leave>", on_remove_button_leave)

# ****************
# upload area
# ****************
def on_upload_area_enter(event):
    main_canvas.itemconfig(upload_area_id, fill= UPLOAD__DOWNLOAD_AREA_HOVER_COLOR)
    root.config(cursor="hand2")


def on_upload_area_leave(event):
    main_canvas.itemconfig(upload_area_id, fill=UPLOAD__DOWNLOAD_AREA_DEFAULT_COLOR)
    root.config(cursor="")

main_canvas.tag_bind(upload_area_id, "<Enter>", on_upload_area_enter)
main_canvas.tag_bind(upload_area_id, "<Leave>", on_upload_area_leave)


# ****************
# download area
# ****************
def on_download_area_enter(event):
    main_canvas.itemconfig(download_area_id, fill=UPLOAD__DOWNLOAD_AREA_HOVER_COLOR)
    root.config(cursor="hand2")


def on_download_area_leave(event):
    main_canvas.itemconfig(download_area_id, fill=UPLOAD__DOWNLOAD_AREA_DEFAULT_COLOR)
    root.config(cursor="")

main_canvas.tag_bind(download_area_id, "<Enter>", on_download_area_enter)
main_canvas.tag_bind(download_area_id, "<Leave>", on_download_area_leave)


# ==========================
# Image Assets
# ==========================

arrow_photo = load_canvas_image(
    main_canvas,
    "assets/img/arrow.png",
    x_position=355,
    y_position=200
)

upload_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/Logo.png",
    x_position=175,
    y_position=200,
    width=40,
    height=40
)

download_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/download_icon.png",
    x_position=525,
    y_position=200,
    width=50,
    height=35
)

whatsapp_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/whatsapp.png",
    x_position=497,
    y_position=430,
    width=24,
    height=24
)

github_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/Github.png",
    x_position=634,
    y_position=430,
    width=24,
    height=24
)

python_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/python.png",
    x_position=355,
    y_position=430,
    width=24,
    height=24
)


root.mainloop()
