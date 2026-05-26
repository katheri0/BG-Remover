import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from UI.main_window import MainWindow

def main():
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    
    # Load stylesheet
    stylesheet_path = Path(__file__).parent / "UI" / "stylesheet.qss"
    if stylesheet_path.exists():
        with open(stylesheet_path, "r") as f:
            stylesheet = f.read()
            # Replace relative paths in QSS with absolute paths (forward slashes required for Qt)
            assets_dir_str = str(Path(__file__).resolve().parent.parent / "assets" / "img").replace("\\", "/")
            stylesheet = stylesheet.replace("assets/img", assets_dir_str)
            app.setStyleSheet(stylesheet)
            
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
# 