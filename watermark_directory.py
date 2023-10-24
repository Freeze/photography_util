#!/usr/bin/env python3

import os
import platform
from PIL import Image, ImageDraw, ImageFont

# ANSI escape codes for terminal colors and bold text
BOLD = "\033[1m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Global variables
WEB_PHOTOS_DIRECTORY = '/home/holden/web_photos'
WATERMARK_TEXT = 'holden@mnowls.com'
FONT_SIZE = 100
TRANSPARENCY = 5  # 2% visibility

# Dictionary to hold font paths based on OS
FONT_PATHS = {
    'Darwin': '/System/Library/Fonts/Helvetica.ttc',  # macOS
    'Linux': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',  # Linux (RHEL9, Rocky Linux)
    'Windows': 'arial.ttf'  # Windows (as a fallback)
}

def get_font_path():
    """Returns the appropriate font path based on the operating system."""
    return FONT_PATHS.get(platform.system(), 'arial.ttf')

def add_watermark(image_path):
    """Adds a watermark to an image."""
    original_image = Image.open(image_path).convert("RGBA")
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
    watermarked.save(image_path)

def main():
    for root, _, files in os.walk(WEB_PHOTOS_DIRECTORY):
        # Delete hidden '.files' created by macOS
        for filename in files:
            if filename.startswith('.'):
                os.remove(os.path.join(root, filename))
                continue

        for filename in files:
            if filename.lower().endswith(('jpg', 'jpeg', 'png')):
                filepath = os.path.join(root, filename)
                print(f"{BOLD}{WHITE}Updating file:{RESET} {GREEN}{filepath}{RESET}", end='\r')
                add_watermark(filepath)

    print("\nWatermarking completed.")

if __name__ == '__main__':
    main()
