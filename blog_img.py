#!/usr/bin/env python3

import argparse
import os
from PIL import Image
import piexif

# Global variables
OUTPUT_DIR = '/Users/holden/dev/blog/content/nov_2023/images/'

def resize_image(input_path, output_path, width=1024):
    """
    Resize the image while maintaining the aspect ratio and best quality.
    """
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        new_height = int(width * aspect_ratio)
        
        img = img.resize((width, new_height), Image.LANCZOS)
        img.save(output_path, quality=95, exif=img.info.get("exif", b""))


def set_metadata(file_path):
    """
    Sets the copyright and contact information in the image metadata.
    """
    exif_dict = piexif.load(file_path)

    # Set Copyright & Artist
    exif_dict["0th"][piexif.ImageIFD.Artist] = "Holden Smith"
    exif_dict["0th"][piexif.ImageIFD.Copyright] = "Holden Smith"

    # Convert dictionary to bytes
    exif_bytes = piexif.dump(exif_dict)

    # Embed EXIF data
    piexif.insert(exif_bytes, file_path)

def main():
    """
    Main function to parse arguments and perform tasks.
    """
    parser = argparse.ArgumentParser(description='Resize image and edit metadata.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input image')
    parser.add_argument('-o', '--output', type=str, required=True, help='Name for the output image')

    args = parser.parse_args()

    input_path = args.input
    output_name = args.output
    output_path = os.path.join(OUTPUT_DIR, output_name)

    resize_image(input_path, output_path)
    set_metadata(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    main()
