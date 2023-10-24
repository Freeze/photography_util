#!/usr/bin/env python3

import os
import json
import argparse
from PIL import Image

# Global Variables
PHOTOS_DIR = "/var/www/hldnio/portfolio/photos"
THUMBNAILS_DIR = os.path.join(PHOTOS_DIR, "thumbnails")
JSON_FILE_PATH = "/var/www/hldnio/portfolio/photos.json"
MAX_SIZE = 10 * 1024 * 1024  # 10 MB
COPYRIGHT = "holden@mnowls.com"

def generate_thumbnail(image_path, thumbnail_path, dimensions):
    """ Create thumbnail files for use on webpage """
    with Image.open(image_path) as img:
        img.thumbnail(dimensions)
        if args.metadata:
            img.info["Copyright"] = COPYRIGHT
        img.save(thumbnail_path)

def resize_large_image(image_path):
    """ Resize large images to a more manageable size"""
    with Image.open(image_path) as img:
        if os.path.getsize(image_path) > MAX_SIZE:
            factor = (MAX_SIZE / os.path.getsize(image_path)) ** 0.5
            new_dimensions = (int(img.width * factor), int(img.height * factor))
            img.thumbnail(new_dimensions)
            if args.metadata:
                img.info["Copyright"] = COPYRIGHT
            img.save(image_path)

def main():
    """ The actual script logic """
    global args
    parser = argparse.ArgumentParser(description='Manage photos and thumbnails.')
    parser.add_argument('-d', '--dimensions', type=str, required=True, help='Thumbnail dimensions in format WIDTHxHEIGHT.')
    parser.add_argument('-f', '--force', action='store_true', help='Force regeneration of thumbnails.')
    parser.add_argument('-s', '--shrink', action='store_true', help='Shrink source images larger than 10MB.')
    parser.add_argument('-m', '--metadata', action='store_true', help='Add copyright metadata.')

    args = parser.parse_args()
    dimensions = tuple(map(int, args.dimensions.lower().split('x')))

    os.makedirs(THUMBNAILS_DIR, exist_ok=True)
    photo_files = []

    for subdir, _, files in os.walk(PHOTOS_DIR):
        if "thumbnails" in subdir:
            continue  # Skip thumbnail directories

        for filename in files:
            if filename.startswith("._"):
                continue  # Skip AppleDouble files or similar
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                sanitized_name = filename.replace(" ", "_")
                relative_subdir = os.path.relpath(subdir, PHOTOS_DIR)
                image_path = os.path.join(subdir, filename)
                thumbnail_path = os.path.join(THUMBNAILS_DIR, relative_subdir, sanitized_name)
                json_entry = os.path.join(relative_subdir, sanitized_name)

                os.makedirs(os.path.join(THUMBNAILS_DIR, relative_subdir), exist_ok=True)

                if args.force or not os.path.exists(thumbnail_path):
                    try:
                        generate_thumbnail(image_path, thumbnail_path, dimensions)
                    except Exception as e:
                        print(f"Skipping {image_path} due to error: {e}")
                        continue

                if args.shrink:
                    try:
                        resize_large_image(image_path)
                    except Exception as e:
                        print(f"Skipping {image_path} due to error: {e}")
                        continue

                photo_files.append(json_entry)

    with open(JSON_FILE_PATH, 'w') as f:
        json.dump({"photoFiles": photo_files}, f)

if __name__ == "__main__":
    main()
