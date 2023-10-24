#!/usr/bin/env python
from pathlib import Path
import os
import sys
import exifread

def check_all_files(directory):
    ''' Loop that finds all files in directory
        and executes the function to organize
        against each file
    '''
    for filename in os.scandir(directory):
        try:
            get_date_from_arw(filename, directory)
        except KeyError:
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)

def get_date_from_arw(filename, directory):
    ''' Function that handles parsing each raw file
        Try/Fail will catch anything that's not a raw file
        Get date from RAW file EXIF, check if directory for date exists
        If directory does not exist, create it
        Move file once directory exists
    '''
    try:
        f = open(filename, 'rb')
        filename = filename.name
        tags = exifread.process_file(f)
        date = str(tags['EXIF DateTimeOriginal'])
        date = date.split(' ', maxsplit=1)[0].replace(':', '-')
        if os.path.exists(date):
            Path(f"{directory}/{filename}").rename(f"{directory}/{date}/{filename}")
        else:
            os.makedirs(date)
            Path(f"{directory}/{filename}").rename(f"{directory}/{date}/{filename}")
        f.close()
    except KeyError: 
        pass


if __name__ == "__main__":
    PHOTO_DIR = "/path/to/directory/full-of-photos/"
    check_all_files(PHOTO_DIR)