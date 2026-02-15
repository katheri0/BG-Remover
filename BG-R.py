import tkinter as tk
# from rembg import remove
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("720x512")
root.title("BG-Remover")

label = tk.Label(root, text="BG-Remover", font=("Arial", 27))
label.pack(padx=20, pady=10)

canvas = tk.Canvas(root, width=720, height=512, bg="white")
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


'''------------- Loading image ---------------'''
# Arrow pointing to the result
Arrow = Image.open("assets/img/arrow.png")
Arrow_photo = ImageTk.PhotoImage(Arrow)

canvas.create_image(
    355, 200,
    image=Arrow_photo
)

#  Add_image

Add_image = Image.open("assets/img/download_icon.png")
Add_image_photo = ImageTk.PhotoImage(Add_image)

canvas.create_image(
    255, 200,
    image=Add_image_photo
)
'''--------------------------------------------'''

'''------------- Shaping The Design ---------------'''
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


# canvas.create_text(
#     175, 200,
#     text="Original Image",
#     font=("Arial", 16),
#     fill="black"
# )


# canvas.create_text(
#     525, 200,
#     text="Result",
#     font=("Arial", 16),
#     fill="black"
# )

canvas.create_text(
    353, 375,
    text="Remove",
    font=("Arial", 14),
    fill="black"
)

canvas.create_text(
    200, 430,
    text="developed by Katheri Saleh using ",
    font=("Arial", 14),
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
    font=("Arial", 14),
    fill="black"
)
# Contacts: 778484033
canvas.create_text(
    660, 430,
    text=" GH:Katheri0",
    font=("Arial", 14),
    fill="black"
)
# Katheri0

'''------------- Loading image ---------------'''

#  downlaod_image
downlaod_image = Image.open("assets/img/download_icon.png")
downlaod_image_photo = ImageTk.PhotoImage(downlaod_image)

canvas.create_image(
    525, 200,
    image=downlaod_image_photo

)

#  Add_image
Add_image = Image.open("assets/img/Logo.png")
resized_logo_image = Add_image.resize((80, 80))
Add_image_photo = ImageTk.PhotoImage(resized_logo_image)

canvas.create_image(
    175, 200,
    image=Add_image_photo
)
'''--------------------------------------------'''
'''----------------------------'''

root.mainloop()
