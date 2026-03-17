# BG-Remover
A desktop-based solution for instant image background removal.

BG-Remover is a Python-powered application designed to isolate the subjects from their backgrounds. Built with a focus on user experience, it combines a modern UI designed in Figma with the reliable performance of Python's libraries (ecosystem).

## Features
Intuitive UI: Clean and modern interface crafted in Figma and implemented with Tkinter (python UI-lib).

Local Processing: Keeps your images private by processing them on your machine.

High Precision: Utilizes optimized Python logic for clean edges and subject detection.

### Architecture
The project follows a standard decoupled flow to ensure the UI remains responsive while the heavy lifting happens in the background.

####  Roadmap & Optimization
While the core functionality is integrated and working, current goals include:

- Logic Optimization: if I found a better model for faster processing speeds I will switch to that.

- Batch Processing: Adding the ability to drop multiple images at once.(Done)

- Optional path for output images . (Done)

- Export Options: Supporting various file formats like  (WebP, BMP, TIFF, etc.). now only PNG. (done)

#### Getting Started :
1. Install dependencies & Launch the app:

```
git clone https://git@github.com:katheri0/BG-Remover.git
cd BG-Remover
pip install -r requirements.txt
python BG-R.py

```

Note: On the very first run, the application will download the U2-Net model (~170MB). Please ensure you have an active internet connection.
