# background_removal_service.py

from pathlib import Path
from rembg import remove
from PIL import Image


def remove_background_from_image(
    input_image_path: str,
    output_image_path: str
) -> str:
    """
    Removes the background from an image and saves the result.

    Args:
        input_image_path: Path to the original image.
        output_image_path: Path where processed image will be saved.

    Returns:
        The output image path.

    Raises:
        FileNotFoundError: If input image does not exist.
        RuntimeError: If background removal fails.
    """

    input_path = Path(input_image_path)
    output_path = Path(output_image_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    try:
        original_image = Image.open(input_path)
        processed_image = remove(original_image)
        processed_image.save(output_path)

    except Exception as error:
        raise RuntimeError(f"Background removal failed: {error}")

    return str(output_path)