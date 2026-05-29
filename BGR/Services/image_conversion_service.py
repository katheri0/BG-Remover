from pathlib import Path
from PIL import Image

def convert_image_format(
    input_image_path: str,
    output_image_path: str,
    export_format: str = "PNG"
) -> str:
    """
    Converts an image to the specified format without removing the background.

    Args:
        input_image_path: Path to the original image.
        output_image_path: Path where processed image will be saved.
        export_format: The target format to convert the image to.

    Returns:
        The output image path.

    Raises:
        FileNotFoundError: If input image does not exist.
        RuntimeError: If image conversion fails.
    """

    input_path = Path(input_image_path)
    output_path = Path(output_image_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    try:
        image = Image.open(input_path)
        
        # Convert RGBA/LA (with alpha) or P (palette) to RGB if target format does not support alpha/palette
        if image.mode in ('RGBA', 'LA', 'P') and export_format.upper() in ('JPG', 'JPEG', 'BMP'):
            image = image.convert('RGB')
            
        image.save(output_path, format=export_format.upper())

    except Exception as error:
        raise RuntimeError(f"Image conversion failed: {error}")

    return str(output_path)
