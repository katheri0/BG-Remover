import tkinter as tk
from UI import state, components, handlers

def build_layout(root):
    title_label = tk.Label(root, text="BG-Remover", font=state.TITLE_FONT, bg=state.WINDOW_BACKGROUND_COLOR)
    title_label.pack(padx=20, pady=10)

    canvas = tk.Canvas(root, width=state.WINDOW_WIDTH, height=state.WINDOW_HEIGHT, bg="white")
    canvas.pack()

    # Create Shapes
    upload_area_id = components.create_rounded_rectangle(canvas, 50, 100, 300, 300, corner_radius=40, fill=state.UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR, outline="black", width=2, dash=(10, 2))
    download_area_id = components.create_rounded_rectangle(canvas, 400, 100, 650, 300, corner_radius=40, fill=state.UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR, outline="black", width=2, dash=(10, 2))
    remove_button_id = components.create_rounded_rectangle(canvas, 270, 350, 430, 400, corner_radius=40, fill=state.REMOVE_BUTTON_DEFAULT_COLOR, outline="black", width=2, dash=(10, 2))
    format_button_id = components.create_rounded_rectangle(canvas, 535, 315, 630, 355, corner_radius=40, fill=state.REMOVE_BUTTON_DEFAULT_COLOR, outline="black", width=2, dash=(10, 2))

    # Text
    upload_text_id = canvas.create_text(175, 260, text="Upload Image", font=("Arial", 16))
    remove_text_id = canvas.create_text(353, 375, text="Remove", font=("Arial", 14))
    format_text_id = canvas.create_text(568, 335, text="Format", font=("Arial", 11))
    
    # Footer Text
    canvas.create_text(200, 430, text="developed by Katheri Saleh using", font=state.DEFAULT_FONT)
    canvas.create_text(30, 430, text="</>", font=("Arial", 25))
    canvas.create_text(505, 430, text="Contacts: 778484033", font=state.DEFAULT_FONT)
    canvas.create_text(680, 430, text="Katheri0", font=state.DEFAULT_FONT)

    # Images (Store references globally in state to prevent GC)
    _, state.arrow_photo = components.load_canvas_image(canvas, "assets/img/arrow.png", 355, 200)
    _, state.upload_icon_photo = components.load_canvas_image(canvas, "assets/img/Logo.png", 175, 200, 48, 48)
    download_icon_id, state.download_icon_photo = components.load_canvas_image(canvas, "assets/img/download_icon.png", 525, 200, 66, 45)
    _, state.whatsapp_photo = components.load_canvas_image(canvas, "assets/img/whatsapp.png", 497, 430, 32, 32)
    _, state.github_photo = components.load_canvas_image(canvas, "assets/img/Github.png", 630, 430, 32, 32)
    _, state.python_photo = components.load_canvas_image(canvas, "assets/img/python.jpg", 358, 430, 28, 28)
    dropdown_photo_id, state.dropdown_photo = components.load_canvas_image(canvas, "assets/img/Format.png", 610, 338, 28, 16)

    # Hover Bindings
    components.bind_hover_group(canvas, "Format_button", format_button_id, [format_button_id, format_text_id, dropdown_photo_id], state.REMOVE_BUTTON_DEFAULT_COLOR, state.REMOVE_BUTTON_HOVER_COLOR, root)
    components.bind_hover_group(canvas, "upload_area", upload_area_id, [upload_area_id, upload_text_id], state.UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR, state.UPLOAD_DOWNLOAD_AREA_HOVER_COLOR, root)
    components.bind_hover_group(canvas, "download_area", download_area_id, [download_area_id, download_icon_id], state.UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR, state.UPLOAD_DOWNLOAD_AREA_HOVER_COLOR, root)
    components.bind_hover_group(canvas, "remove_button", remove_button_id, [remove_button_id, remove_text_id], state.REMOVE_BUTTON_DEFAULT_COLOR, state.REMOVE_BUTTON_HOVER_COLOR, root)

    # Clicks
    canvas.tag_bind("upload_area", "<Button-1>", lambda e: handlers.handle_upload_click(canvas, upload_text_id))
    canvas.tag_bind("remove_button", "<Button-1>", lambda e: handlers.handle_remove_click(root, canvas))
    canvas.tag_bind("download_area", "<Button-1>", lambda e: handlers.handle_download_area_click(canvas, download_icon_id))
    canvas.tag_bind("Format_button", "<Button-1>", lambda e: handlers.show_format_menu(e, root, canvas, format_text_id))

    return canvas