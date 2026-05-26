from PIL import Image
from typing import Dict
import os


SUPPORTED_IMAGE_FORMATS = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")


def load_medical_image(image_path: str) -> Dict[str, str]:
    """
    Validates and loads a medical image.

    Returns:
    {
        "path": str,
        "format": str,
        "mode": str,
        "size": (width, height)
    }
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    if not image_path.lower().endswith(SUPPORTED_IMAGE_FORMATS):
        raise ValueError("Unsupported image format")

    image = Image.open(image_path)

    return {
        "path": image_path,
        "format": image.format,
        "mode": image.mode,
        "size": image.size
    }
