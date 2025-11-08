ASCII Art Generator
Convert your images into beautiful black & white or color ASCII art using Python, with fully customizable options!

Features
- Select between black & white or colored ASCII output.
- Choose art style: Normal or Sketch (contour effect).
- Pick your font: Consolas, Courier New, DejaVu Sans Mono (all bundled).
- Font size selection for output image.
- Portable – all fonts required for rendering included in the fonts directory.
- Cross-platform: Works on Windows, Linux, and Mac.
- Outputs high-quality ASCII art as image (output_asciiart.jpg).

Getting Started
1. Clone the repository
bash
git clone https://github.com/manoj181319/Ascii_art-generator
2. Install Dependencies
This project requires Python 3, PIL (Pillow):

bash
pip install pillow
3. Project Structure
text
ascii_art.py
fonts/
    consola.ttf
    cour.ttf
    DejaVuSansMono.ttf
test.jpg              # (or your own image)
output_asciiart.jpg   # (generated on run)
4. Usage
Run the script:

bash
python ascii_art.py

Follow the interactive prompts:

- Choose output mode (bw/color)
- Select art style (normal/sketch)
- Pick a font (1/2/3)
- Set font size

Output will be saved as output_asciiart.jpg in your working directory.

- Notes:
Do not remove or rename the fonts folder or the font files within.

Script uses test.jpg by default; replace this with your own image if desired.

For best visual results, use clear and high-contrast input images.

- Changelog (latest version):
Added color/grayscale and sketch/normal mode selection.

Improved font and output customization.

Modularized image processing pipeline.

Bundled all required font files for cross-platform use.