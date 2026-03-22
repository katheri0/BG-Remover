import tkinter as tk

selected_files_paths = []
selected_image_preview = None
result_image_preview = None
output_directory = None
selected_export_format = "png"

# Constants
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 512
WINDOW_BACKGROUND_COLOR = "#FFFFFF"
UPLOAD_DOWNLOAD_AREA_DEFAULT_COLOR = "#FFF0CF"
UPLOAD_DOWNLOAD_AREA_HOVER_COLOR = "#FDE6A8"
REMOVE_BUTTON_DEFAULT_COLOR = "#FFF0CF"
REMOVE_BUTTON_HOVER_COLOR = "#F7D88A"
TITLE_FONT = ("Arial", 27)
DEFAULT_FONT = ("Arial", 14)