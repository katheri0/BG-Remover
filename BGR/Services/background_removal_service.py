# background_removal_service.py

from pathlib import Path
from rembg import remove, new_session
from PIL import Image
import onnxruntime as ort

# Detect available ONNX Runtime providers
available_providers = ort.get_available_providers()

# Prioritize GPU/accelerated providers if they are available
preferred_providers = [
    'TensorrtExecutionProvider',
    'CUDAExecutionProvider',
    'DmlExecutionProvider',
    'CoreMLExecutionProvider',
]

# Keep only the available ones in priority order
providers = [p for p in preferred_providers if p in available_providers]

# Always append CPU as a safe fallback
if 'CPUExecutionProvider' not in providers:
    providers.append('CPUExecutionProvider')

# Create a shared session to improve performance on subsequent calls
_session = new_session('u2net', providers=providers)


def remove_background_from_image(
    input_image_path: str,
    output_image_path: str,
    export_format: str = "PNG"
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
        processed_image = remove(original_image, session=_session)
        processed_image.save(output_path, format=export_format.upper())

    except Exception as error:
        raise RuntimeError(f"Background removal failed: {error}")

    return str(output_path)