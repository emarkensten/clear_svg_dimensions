# SVG Dimension Cleaner

## Description

SVG Dimension Cleaner is a Python script designed to automate the process of removing `width` and `height` attributes from SVG files. This tool is particularly useful for developers and designers who work with SVG files and need them to be scalable without fixed dimensions.

## Features

- **Automated Processing**: Batch processes all SVG files in a specified directory.
- **Safe and Non-Destructive**: Original SVG files remain unchanged; modified files are saved in a separate `/parsed/` subdirectory.
- **Error Handling**: The script identifies files that could not be processed and reports any errors encountered.

## Requirements

- Python 3.x

## Installation

No installation is necessary. Simply download `clear_svg_dimensions.py` to your local machine.

## Usage

To use the script, navigate to the directory where `clear_svg_dimensions.py` is located and run the following command in the terminal:

```bash
python clear_svg_dimensions.py /path/to/svg/directory
