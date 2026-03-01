import tkinter as tk
from PIL import Image, ImageTk


# ==========================
# Window Configuration
# ==========================

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 512
WINDOW_BACKGROUND_COLOR = "#FFFFFF"

UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR = "#FFF0CF"
UPLOAD_DOWNLOAD_AREA_HOVER_COLOR = "#FDE6A8"

REMOVE_BUTTON_DEFAULT_COLOR = "#FFF0CF"
REMOVE_BUTTON_HOVER_COLOR = "#F7D88A"

TITLE_FONT = ("Arial", 27)
DEFAULT_FONT = ("Arial", 14)


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
    image_id = canvas.create_image(x_position, y_position, image=photo_image)

    return image_id, photo_image  # return both


def bind_hover_group(canvas, tag_name, rectangle_id, grouped_item_ids,
                     default_color, hover_color, root_window):

    # Assign shared tag
    for item_id in grouped_item_ids:
        canvas.addtag_withtag(tag_name, item_id)

    def on_enter(event):
        canvas.itemconfig(rectangle_id, fill=hover_color)
        root_window.config(cursor="hand2")

    def on_leave(event):
        canvas.itemconfig(rectangle_id, fill=default_color)
        root_window.config(cursor="")

    canvas.tag_bind(tag_name, "<Enter>", on_enter)
    canvas.tag_bind(tag_name, "<Leave>", on_leave)


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
    50, 100, 300, 300,
    corner_radius=40,
    fill=UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR,
    outline="black",
    width=2,
    dash=(10, 2)
)

download_area_id = create_rounded_rectangle(
    main_canvas,
    400, 100, 650, 300,
    corner_radius=40,
    fill=UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR,
    outline="black",
    width=2,
    dash=(10, 2)
)

remove_button_id = create_rounded_rectangle(
    main_canvas,
    270, 350, 430, 400,
    corner_radius=40,
    fill=REMOVE_BUTTON_DEFAULT_COLOR,
    outline="black",
    width=2,
    dash=(10, 2)
)


# ==========================
# Text Elements
# ==========================

upload_text_id = main_canvas.create_text(
    175, 260,
    text="Upload Image",
    font=("Arial", 16)
)

remove_text_id = main_canvas.create_text(
    353, 375,
    text="Remove",
    font=("Arial", 14)
)

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
# Image Assets
# ==========================

arrow_id, arrow_photo = load_canvas_image(
    main_canvas,
    "assets/img/arrow.png",
    355, 200
)

upload_icon_id, upload_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/Logo.png",
    175, 200,
    width=40,
    height=40
)

download_icon_id, download_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/download_icon.png",
    525, 200,
    width=50,
    height=35
)

whatsapp_id, whatsapp_photo = load_canvas_image(
    main_canvas,
    "assets/img/whatsapp.png",
    497, 430,
    width=24,
    height=24
)

github_id, github_photo = load_canvas_image(
    main_canvas,
    "assets/img/Github.png",
    634, 430,
    width=24,
    height=24
)

python_id, python_photo = load_canvas_image(
    main_canvas,
    "assets/img/python.png",
    355, 430,
    width=24,
    height=24
)


# ==========================
# Hover Bindings (Automated)
# ==========================

bind_hover_group(
    canvas=main_canvas,
    tag_name="upload_area",
    rectangle_id=upload_area_id,
    grouped_item_ids=[upload_area_id, upload_text_id, upload_icon_id],
    default_color=UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR,
    hover_color=UPLOAD_DOWNLOAD_AREA_HOVER_COLOR,
    root_window=root
)

bind_hover_group(
    canvas=main_canvas,
    tag_name="download_area",
    rectangle_id=download_area_id,
    grouped_item_ids=[download_area_id, download_icon_id],
    default_color=UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR,
    hover_color=UPLOAD_DOWNLOAD_AREA_HOVER_COLOR,
    root_window=root
)

bind_hover_group(
    canvas=main_canvas,
    tag_name="remove_button",
    rectangle_id=remove_button_id,
    grouped_item_ids=[remove_button_id, remove_text_id],
    default_color=REMOVE_BUTTON_DEFAULT_COLOR,
    hover_color=REMOVE_BUTTON_HOVER_COLOR,
    root_window=root
)


root.mainloop()
