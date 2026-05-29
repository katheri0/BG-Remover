from PyQt6.QtCore import QThread, pyqtSignal
from pathlib import Path
from Services.background_removal_service import remove_background_from_image
from Services.image_conversion_service import convert_image_format

class BackgroundRemovalWorker(QThread):
    progress = pyqtSignal(int, int) # current, total
    finished = pyqtSignal(str) # output string
    error = pyqtSignal(str) # error message

    def __init__(self, file_paths, output_directory, export_format):
        super().__init__()
        self.file_paths = file_paths
        self.output_directory = output_directory
        self.export_format = export_format

    def run(self):
        total = len(self.file_paths)
        for index, file_path in enumerate(self.file_paths, 1):
            input_path = Path(file_path)
            
            if self.output_directory:
                save_folder = Path(self.output_directory)
            else:
                save_folder = input_path.parent
                
            output_path = save_folder / f"{input_path.stem}_no_bg.{self.export_format}"

            self.progress.emit(index, total)

            try:
                # remove_background_from_image performs the IO and rembg process
                remove_background_from_image(str(input_path), str(output_path), self.export_format)
            except Exception as e:
                self.error.emit(f"Error processing {input_path.name}: {e}")
                
        self.finished.emit("Batch Complete!")


class ImageConversionWorker(QThread):
    progress = pyqtSignal(int, int) # current, total
    finished = pyqtSignal(str) # output string
    error = pyqtSignal(str) # error message

    def __init__(self, file_paths, output_directory, export_format):
        super().__init__()
        self.file_paths = file_paths
        self.output_directory = output_directory
        self.export_format = export_format

    def run(self):
        total = len(self.file_paths)
        for index, file_path in enumerate(self.file_paths, 1):
            input_path = Path(file_path)
            
            if self.output_directory:
                save_folder = Path(self.output_directory)
            else:
                save_folder = input_path.parent
                
            output_path = save_folder / f"{input_path.stem}_converted.{self.export_format}"

            self.progress.emit(index, total)

            try:
                # convert_image_format performs the IO and conversion process
                convert_image_format(str(input_path), str(output_path), self.export_format)
            except Exception as e:
                self.error.emit(f"Error processing {input_path.name}: {e}")
                
        self.finished.emit("Batch Conversion Complete!")
