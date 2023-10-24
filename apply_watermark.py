#!/usr/bin/env python3

import os
import platform
from PIL import Image, ImageDraw, ImageFont

# Global variables
BASE_DIRECTORY = '/Users/holden/dev/watermark/'
INPUT_FILE_NAME = 'pixel.jpg'
OUTPUT_FILE_NAME = 'wm_pixel.jpg'
INPUT_FILE_PATH = os.path.join(BASE_DIRECTORY, INPUT_FILE_NAME)
OUTPUT_FILE_PATH = os.path.join(BASE_DIRECTORY, OUTPUT_FILE_NAME)
WATERMARK_TEXT = 'holden@mnowls.com'
FONT_SIZE = 100
TRANSPARENCY = 13  # 5% visibility

# Dictionary to hold font paths based on OS
FONT_PATHS = {
    'Darwin': '/System/Library/Fonts/Helvetica.ttc',  # macOS
    'Linux': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',  # Linux (RHEL9, Rocky Linux)
    'Windows': 'arial.ttf'  # Windows (as a fallback)
}

def get_font_path():
    """Returns the appropriate font path based on the operating system."""
    return FONT_PATHS.get(platform.system(), 'arial.ttf')

def add_watermark():
    """Adds a watermark to an image."""
    if not os.path.exists(INPUT_FILE_PATH):
        print(f"Error: Input file '{INPUT_FILE_PATH}' not found.")
        return

    original_image = Image.open(INPUT_FILE_PATH).convert("RGBA")
    width, height = original_image.size
    txt = Image.new('RGBA', original_image.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txt)

    try:
        fnt = ImageFont.truetype(get_font_path(), FONT_SIZE)
    except IOError:
        fnt = ImageFont.load_default()
        print("Warning: Could not load specified TrueType Font. Using default PIL font.")

    # Manually adjust the position to make watermark text appear centered
    x = width // 3
    y = height // 3

    d.text((x, y), WATERMARK_TEXT, font=fnt, fill=(255, 255, 255, TRANSPARENCY))
    watermarked = Image.alpha_composite(original_image, txt)
    watermarked = watermarked.convert("RGB")
    watermarked.save(OUTPUT_FILE_PATH)

if __name__ == '__main__':
    add_watermark()
