from PIL import Image, ImageTk

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
    return image_id, photo_image

def bind_hover_group(canvas, tag_name, rectangle_id, grouped_item_ids, default_color, hover_color, root_window):
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