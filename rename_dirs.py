#!/usr/bin/env python
import os
import sys
import argparse
from pathlib import Path

def rename_files():
    for d in os.walk(os.getcwd()):
        dirname = d[0]
        dirname_display = dirname.split('/')[-1]
        num_folder_args = len(dirname.split('-'))
        if num_folder_args == 3:
            print(f"** RENAMING DIRECTORY {dirname_display} **")
            location = input('Where were these photos taken?\n')
            subject = input('What are these photos of?\n') 
            new_name = f"{dirname} - {location} - {subject}"
            new_name_display = f"{dirname_display} - {location} - {subject}"
            print(f"New Name Will Be: {new_name_display}\n\n")
            Path(dirname).rename(new_name)
        elif num_folder_args == 5:
            pass

if __name__ == "__main__":
    rename_files()
