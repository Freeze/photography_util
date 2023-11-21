# Photo Management Python Scripts

A collection of Python scripts developed to assist in managing a photography portfolio/library. These scripts include watermarking, resizing, metadata addition, and more.

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [To-Do](#to-do)

## Description

### apply_watermark.py

- **Purpose**: Applies a watermark to a single photo file.
- **Note**: This was the original script before `watermark_directory.py` was developed. Use this for testing watermark looks on individual files.

### watermark_directory.py

- **Purpose**: Applies a watermark to all photos in a specified directory.
- **Warning**: The logging mechanism is currently not stable; proceed with caution if you intend to use this script for your needs.

### blog_img.py

- **Purpose**: Resizes and adds copyright metadata to a single photo file. The file is then saved to the output directory specified in the script.
- **Note**: This script is generally run via an alias in the `.zshrc` file.

### portfolio_sync.py

- **Purpose**: Performs various actions on a directory of images, including:
  - Creating static thumbnails with dimensions specified by the `-d` flag.
  - Shrinking files over 10 MB to conserve bandwidth.
  - Adding email metadata to files.

### sort_into_subdirs.py

- **Purpose**: Takes a directory of files and sorts them into subdirectories based on their dates.
- **Note**: This script is particularly useful if you find yourself with a messy directory structure, such as after a sync gone wrong.

### rename_dirs.py

- **Purpose**: Rename directories from `YYYY-MM-DD` to `YYYY-MM-DD - <LOCATION> - <DESCR>`.
- **Note**: I take a lot of pictures and sometimes I forget what's what. This parses all subdirs in a dir and prompts you to rename them one by one.

## Installation

Clone this repository to your local machine and navigate to the directory containing the scripts.

```bash
git clone git@github.com:Freeze/photography_util.git>
cd photography_util>
```

Make sure to install any dependencies that are required for these scripts.

```bash
pip install -r requirements.txt
```

## Usage

Each script can be run from the command line and includes its own set of flags for customization.

```bash
python3 <script_name>.py [options]
```

For detailed usage instructions for each script, see the individual script files.

## Contributing

If you find a bug or would like to contribute, feel free to create a pull request.

## License

This project is licensed under the MIT License.

## To-Do

- [ ] Package all scripts to make them more portable and manageable.
- [ ] Not abandon this like everything else I put on GitHub!
- [ ] Document any caveats with package versions - not everything always works perfect on every machine.