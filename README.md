# ASCII Art Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A small Python project to generate ASCII art from text or images. This repository provides a simple command-line tool and examples to convert input (text or images) into readable ASCII art that can[...] 

## Features
- Select between black & white or colored ASCII output.
- Choose art style: Normal or Sketch (contour effect).
- Pick your font: Consolas, Courier New, DejaVu Sans Mono (all bundled).
- Font size selection for output image.
- Portable – all fonts required for rendering included in the fonts directory.
- Cross-platform: Works on Windows, Linux, and Mac.
- Outputs high-quality ASCII art as image (output_asciiart.jpg).

## Requirements
- Python 3
- Pillow (for image → ASCII functionality)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/manoj181319/Ascii_art-generator
cd Ascii_art-generator
```

2. Install dependencies:
```bash
pip install pillow
```
## Project Structure:
```bash
ascii_art.py
fonts/
    consola.ttf
    cour.ttf
    DejaVuSansMono.ttf
test.jpg              # (or your own image)
output_asciiart.jpg   # (generated on run)
```

## Usage
Run the script:
```bash
python ascii_art.py
```
Follow the interactive prompts:
- Choose output mode (bw/color)
- Select art style (normal/sketch)
- Pick a font (1/2/3)
- Set font size
Output will be saved as output_asciiart.jpg in your working directory.

## Notes
- Do not remove or rename the fonts folder or the font files within.
- Script uses test.jpg by default; replace this with your own image if desired.
- For best visual results, use clear and high-contrast input images.

## Changelog (latest version)
- Added color/grayscale and sketch/normal mode selection.
- Added OpenCV powered sketch effect.
- Improved font and output customization.
- Modularized image processing pipeline.
- Bundled all required font files for cross-platform use.
