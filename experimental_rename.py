#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
import shutil

def create_delete_me_folder():
    """Create DELETE_ME folder if it doesn't exist."""
    delete_me_path = os.path.join(os.getcwd(), "DELETE_ME")
    if not os.path.exists(delete_me_path):
        os.mkdir(delete_me_path)

def move_files(source_dir, target_dir):
    """Move files from source directory to target directory."""
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        if not os.path.exists(target_file):
            shutil.move(source_file, target_file)
        else:
            # If the file already exists in the target directory, ignore it
            print(f"Ignoring duplicate file: {filename}")

def rename_files():
    """Rename files in directories that do not match the desired format."""
    for root, dirs, files in os.walk(os.getcwd()):
        for dirname in dirs:
            dirname_display = dirname.split('/')[-1]
            num_folder_args = len(dirname.split('-'))
            if num_folder_args == 3:
                target_dir = os.path.join(os.getcwd(), dirname)
                desired_dir = os.path.join(os.getcwd(), dirname_display)
                existing_dirs = [d for d in os.listdir(os.getcwd()) if d.startswith(dirname_display) and len(d.split('-')) == 5]
                if existing_dirs:
                    existing_dir = os.path.join(os.getcwd(), existing_dirs[0])
                    print(f"Moving files from {dirname_display} to {existing_dir}")
                    move_files(target_dir, existing_dir)
                    shutil.move(target_dir, os.path.join(os.getcwd(), "DELETE_ME", dirname_display))
                else:
                    print(f"** RENAMING DIRECTORY {dirname_display} **")
                    location = input('Where were these photos taken?\n')
                    subject = input('What are these photos of?\n')
                    new_name = f"{dirname_display} - {location} - {subject}"
                    new_name_display = f"{dirname_display} - {location} - {subject}"
                    print(f"New Name Will Be: {new_name_display}\n\n")
                    os.rename(target_dir, os.path.join(os.getcwd(), new_name))
            elif num_folder_args == 5:
                pass

if __name__ == "__main__":
    create_delete_me_folder()
    rename_files()
