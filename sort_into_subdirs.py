#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import exifread

def check_all_files(directory):
    ''' 
    Loop through all files in the directory and organize them.
    '''
    for entry in os.scandir(directory):
        if entry.is_file() and not entry.name.startswith('.'):
            try:
                get_date_from_arw(entry, directory)
            except KeyError:
                continue
            except KeyboardInterrupt:
                sys.exit(1)

def get_date_from_arw(file_entry, directory):
    ''' 
    Parse each raw file and organize based on EXIF date.
    '''
    try:
        with open(file_entry.path, 'rb') as file:
            tags = exifread.process_file(file)
            date = str(tags['EXIF DateTimeOriginal']).split(' ', 1)[0].replace(':', '-')
            target_dir = os.path.join(directory, date)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            new_path = os.path.join(target_dir, file_entry.name)
            os.rename(file_entry.path, new_path)
    except KeyError:
        pass

if __name__ == "__main__":
    current_directory = os.getcwd()
    check_all_files(current_directory)

