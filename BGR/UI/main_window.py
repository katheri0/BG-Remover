import os
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QComboBox, QFileDialog, QSizePolicy, QToolButton
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

from UI.worker import BackgroundRemovalWorker

ASSETS_DIR = Path(__file__).resolve().parent.parent.parent / "assets" / "img"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BG-Remover")
        self.setMinimumSize(720, 512)
        self.resize(720, 512)
        
        self.selected_files_paths = []
        self.output_directory = None
        
        self._init_ui()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 20, 40, 20)
        main_layout.setSpacing(15)

        # Title
        self.title_label = QLabel("BG-Remover")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Content Area
        content_layout = QHBoxLayout()
        content_layout.setSpacing(40)
        
        # --- Left Side ---
        left_layout = QVBoxLayout()
        
        self.upload_btn = QPushButton("Upload Image\n\n\n\n")
        self.upload_btn.setIcon(QIcon(str(ASSETS_DIR / "Logo.png")))
        self.upload_btn.setIconSize(QSize(48, 48))
        self.upload_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.upload_btn.clicked.connect(self.handle_upload)
        
        left_buttons_layout = QHBoxLayout()
        self.convertor_btn = QPushButton("Convertor")
        self.convertor_btn.setObjectName("actionButton")
        self.convertor_btn.setFixedHeight(50)
        
        self.remove_btn = QPushButton("Remove")
        self.remove_btn.setObjectName("actionButton")
        self.remove_btn.setFixedHeight(50)
        self.remove_btn.clicked.connect(self.handle_remove)
        
        left_buttons_layout.addWidget(self.convertor_btn)
        left_buttons_layout.addWidget(self.remove_btn)
        
        left_layout.addWidget(self.upload_btn)
        left_layout.addLayout(left_buttons_layout)
        
        # --- Right Side ---
        right_layout = QVBoxLayout()
        
        self.download_btn = QPushButton("")
        self.download_btn.setIcon(QIcon(str(ASSETS_DIR / "download_icon.png")))
        self.download_btn.setIconSize(QSize(66, 45))
        self.download_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.download_btn.clicked.connect(self.handle_download_area)
        
        right_bottom_layout = QHBoxLayout()
        
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "WEBP", "BMP", "TIFF", "JPG"])
        self.format_combo.setFixedHeight(40)
        self.format_combo.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        
        right_bottom_layout.addWidget(self.status_label, stretch=1)
        right_bottom_layout.addWidget(self.format_combo)
        
        right_layout.addWidget(self.download_btn)
        right_layout.addLayout(right_bottom_layout)
        
        # Add to content
        content_layout.addLayout(left_layout, stretch=1)
        content_layout.addLayout(right_layout, stretch=1)
        
        main_layout.addLayout(content_layout, stretch=1)
        
        # Footer
        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(0, 10, 0, 0)
        
        dev_label = QLabel("developed by Katheri Saleh using")
        
        code_icon = QLabel("</>")
        code_icon.setStyleSheet("font-size: 25px; font-weight: bold;")
        
        python_icon = QLabel()
        python_icon.setPixmap(QPixmap(str(ASSETS_DIR / "python.jpg")).scaled(28, 28, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
        contact_label = QLabel("Contacts: 778484033 | Katheri0")
        
        whatsapp_icon = QLabel()
        whatsapp_icon.setPixmap(QPixmap(str(ASSETS_DIR / "whatsapp.png")).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
        github_icon = QLabel()
        github_icon.setPixmap(QPixmap(str(ASSETS_DIR / "Github.png")).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
        footer_layout.addWidget(code_icon)
        footer_layout.addWidget(dev_label)
        footer_layout.addWidget(python_icon)
        footer_layout.addStretch()
        footer_layout.addWidget(whatsapp_icon)
        footer_layout.addWidget(contact_label)
        footer_layout.addWidget(github_icon)
        
        main_layout.addLayout(footer_layout)

    def handle_upload(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Images",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_paths:
            self.selected_files_paths = file_paths
            # Show preview for first image on button
            pixmap = QPixmap(self.selected_files_paths[0]).scaled(120, 90, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.upload_btn.setIcon(QIcon(pixmap))
            self.upload_btn.setIconSize(self.upload_btn.rect().size()) # Make image fill button nicely
            self.upload_btn.setText(f"{len(self.selected_files_paths)} files loaded")

    def handle_download_area(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if directory:
            self.output_directory = directory
            folder_name = Path(directory).name
            self.download_btn.setIcon(QIcon()) # Remove icon
            self.download_btn.setText(f"Saving to:\n/{folder_name}")

    def handle_remove(self):
        if not self.selected_files_paths:
            self.status_label.setText("No images uploaded!")
            self.status_label.setStyleSheet("color: red;")
            return
            
        export_format = self.format_combo.currentText().lower()
        
        self.remove_btn.setEnabled(False)
        self.upload_btn.setEnabled(False)
        self.status_label.setText("Starting...")
        self.status_label.setStyleSheet("color: #333333;")
        
        self.worker = BackgroundRemovalWorker(self.selected_files_paths, self.output_directory, export_format)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.removal_finished)
        self.worker.error.connect(self.removal_error)
        self.worker.start()

    def update_progress(self, current, total):
        self.status_label.setText(f"Processing {current}/{total}...")
        
    def removal_finished(self, message):
        self.status_label.setText(message)
        self.status_label.setStyleSheet("color: green;")
        self.remove_btn.setEnabled(True)
        self.upload_btn.setEnabled(True)
        
    def removal_error(self, message):
        self.status_label.setText("An error occurred.")
        self.status_label.setStyleSheet("color: red;")
        self.remove_btn.setEnabled(True)
        self.upload_btn.setEnabled(True)
        print(message)
