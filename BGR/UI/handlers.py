import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageTk
from UI import state
from Services.background_removal_service import remove_background_from_image

def handle_upload_click(canvas, upload_text_id):
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not file_paths:
        return

    state.selected_files_paths = list(file_paths)
    image = Image.open(state.selected_files_paths[0])
    image.thumbnail((120, 90))
    state.selected_image_preview = ImageTk.PhotoImage(image)
    canvas.create_image(175, 180, image=state.selected_image_preview)
    canvas.itemconfig(upload_text_id, text=f"{len(state.selected_files_paths)} files loaded")

def handle_download_area_click(canvas, download_icon_id):
    selected_dir = filedialog.askdirectory(title="Select Output Folder")
    if selected_dir:
        state.output_directory = selected_dir
        folder_name = Path(selected_dir).name
        canvas.itemconfig(download_icon_id, state='hidden')
        canvas.delete("dir_label")
        canvas.create_text(
            525, 200,
            text=f"Saving to: /{folder_name}",
            font=("Arial", 14),
            fill="#333333",
            tags="dir_label"
        )

def handle_remove_click(root, canvas):
    if not state.selected_files_paths:
        return

    status_tag = canvas.create_text(350, 320, text="Starting...", font=state.DEFAULT_FONT)
    root.update_idletasks()

    for index, file_path in enumerate(state.selected_files_paths, 1):
        input_path = Path(file_path)
        save_folder = Path(state.output_directory) if state.output_directory else input_path.parent
        output_path = save_folder / f"{input_path.stem}_no_bg.{state.selected_export_format}"
        
        canvas.itemconfig(status_tag, text=f"Processing {index}/{len(state.selected_files_paths)}...")
        root.update()

        try:
            remove_background_from_image(str(input_path), str(output_path), state.selected_export_format)
        except Exception as e:
            print(f"Error: {e}")

    canvas.itemconfig(status_tag, text="Batch Complete!", fill="green")

def show_format_menu(event, root, canvas, format_text_id):
    format_menu = tk.Menu(root, tearoff=0, bg="#FFF0CF", activebackground="#F7D88A", font=("Arial", 10))
    supported_formats = [("PNG", "png"), ("WebP", "webp"), ("BMP", "bmp"), ("TIFF", "tiff"), ("JPEG", "jpg")]

    for label, ext in supported_formats:
        format_menu.add_command(
            label=label, 
            command=lambda e=ext: set_selected_export_format(e, canvas, format_text_id)
        )
    format_menu.post(event.x_root, event.y_root)

def set_selected_export_format(extension, canvas, format_text_id):
    state.selected_export_format = extension
    canvas.itemconfig(format_text_id, text=extension.upper())