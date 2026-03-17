# BG-R.py (font-end UI )
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
from background_removal_service import remove_background_from_image
from tkinter import filedialog

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

# no zoom-in or out
root.resizable(False, False)
root.attributes("-toolwindow", False)

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
# globel - variables
# ==========================
selected_files_paths = []
selected_image_preview = None
result_image_preview = None
output_directory = None
selected_export_format = "png"

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
# 540, 300,   # left_x, top_y
# 650, 340,   # right_x, bottom_y
format_button_id = create_rounded_rectangle(
    main_canvas,
    535, 315,   # left_x, top_y
    630, 355,   # right_x, bottom_y
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


format_text_id = main_canvas.create_text(
    568, 335,
    text="Format",
    font=("Arial", 11)
)
# ==========================
# Image Assets
# ==========================

# 16 px
# 24 px 12px
# 32 px
# 48 px
arrow_id, arrow_photo = load_canvas_image(
    main_canvas,
    "assets/img/arrow.png",
    355, 200
)

upload_icon_id, upload_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/Logo.png",
    175, 200,
    width=48,
    height=48
)

download_icon_id, download_icon_photo = load_canvas_image(
    main_canvas,
    "assets/img/download_icon.png",
    525, 200,
    width=66,
    height=45
)

whatsapp_id, whatsapp_photo = load_canvas_image(
    main_canvas,
    "assets/img/whatsapp.png",
    497, 430,
    width=32,
    height=32
)

github_id, github_photo = load_canvas_image(
    main_canvas,
    "assets/img/Github.png",
    630, 430,
    width=32,
    height=32
)

python_id, python_photo = load_canvas_image(
    main_canvas,
    "assets/img/python.jpg",
    358, 430,
    width=28,
    height=28
)

dropdown_photo_id, dropdown_photo = load_canvas_image(
    main_canvas,
    "assets/img/Format.png",
    610, 338,
    width=28,
    height=16
)
# ==========================
# Upload Logic
# ==========================


def handle_upload_click(event=None):
    global selected_files_paths, selected_image_preview

    # Changed to askopenfilenames to allow multiple selection
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not file_paths:
        return

    selected_files_paths = list(file_paths)  # Store the list

    # Show preview of the FIRST image in the batch
    image = Image.open(selected_files_paths[0])
    image.thumbnail((120, 90))
    selected_image_preview = ImageTk.PhotoImage(image)
    main_canvas.create_image(175, 180, image=selected_image_preview)

    # Update text to show count
    main_canvas.itemconfig(
        upload_text_id, text=f"{len(selected_files_paths)} files loaded")


# ==========================
# Setting a output path Logic
# ==========================

def handle_download_area_click(event=None):
    global output_directory

    selected_dir = filedialog.askdirectory(title="Select Output Folder")

    if selected_dir:
        output_directory = selected_dir
        folder_name = Path(selected_dir).name

        main_canvas.itemconfig(download_icon_id, state='hidden')

        # remove previous label
        main_canvas.delete("dir_label")

        main_canvas.create_text(
            525, 200,
            text=f"Saving to: /{folder_name}",
            font=("Arial", 14),
            fill="#333333",
            tags="dir_label"
        )

# ==========================
# Updated Remove Logic (Batch + Using Optional Path)
# ==========================
#  output_path


def handle_remove_click(event=None):
    global result_image_preview

    if not selected_files_paths:
        return

    status_tag = main_canvas.create_text(
        350, 320, text="Starting...", font=DEFAULT_FONT)
    root.update_idletasks()  # Force UI to show "Processing..."
    processed_count = 0

    for index, file_path in enumerate(selected_files_paths, 1):
        input_path = Path(file_path)
        # LOGIC: If output_directory is set, use it. Otherwise, use source folder.
        if output_directory:
            save_folder = Path(output_directory)
        else:
            save_folder = input_path.parent

        output_path = save_folder / \
            f"{input_path.stem}_no_bg.{selected_export_format}"
        # processed_count
        main_canvas.itemconfig(
            status_tag, text=f"Processing {index}/{len(selected_files_paths)}...")
        root.update()

        try:
            result_path = remove_background_from_image(
                str(input_path),
                str(output_path),
                selected_export_format
            )

            processed_count += 1
            # Update status text per image
            root.update_idletasks()

        except Exception as e:
            print(f"Error: {e}")

    main_canvas.itemconfig(status_tag, text="Batch Complete!", fill="green")

# ==========================
# Format btn Logic
# ==========================


def show_format_menu(event=None):

    format_menu = tk.Menu(
        root,
        tearoff=0,
        bg="#FFF0CF",
        fg="black",
        activebackground="#F7D88A",
        activeforeground="black",
        font=("Arial", 10)
    )

    supported_formats = [
        ("PNG", "png"),
        ("WebP", "webp"),
        ("BMP", "bmp"),
        ("TIFF", "tiff"),
        ("JPEG", "jpg")
    ]

    for label, ext in supported_formats:
        format_menu.add_command(
            label=label,
            command=lambda extension=ext: set_selected_export_format(extension)
        )

    format_menu.post(event.x_root, event.y_root)


def set_selected_export_format(extension: str):
    global selected_export_format

    selected_export_format = extension

    # Update the button text so user sees the selection
    main_canvas.itemconfig(format_text_id, text=extension.upper())

# ==========================
# Hover Bindings (Automated)
# ==========================


bind_hover_group(
    canvas=main_canvas,
    tag_name="Format_button",
    rectangle_id=format_button_id,
    grouped_item_ids=[format_button_id, format_text_id, dropdown_photo_id],
    default_color=REMOVE_BUTTON_DEFAULT_COLOR,
    hover_color=REMOVE_BUTTON_HOVER_COLOR,
    root_window=root
)

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

main_canvas.tag_bind("upload_area", "<Button-1>", handle_upload_click)
main_canvas.tag_bind("remove_button", "<Button-1>", handle_remove_click)
main_canvas.tag_bind("download_area", "<Button-1>", handle_download_area_click)
main_canvas.tag_bind("Format_button", "<Button-1>", show_format_menu)
root.mainloop()
