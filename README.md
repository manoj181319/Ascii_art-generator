# ASCII Art Generator

A small Python project to generate ASCII art from text or images. This repository provides a simple command-line tool and examples to convert input (text or images) into readable ASCII art that can be printed to the terminal or saved to a file.

Features
- Convert text to ASCII art using built-in fonts.
- Convert images to grayscale ASCII art.
- Save output to a file or print to stdout.
- Minimal dependencies (pure Python or Pillow for image support).

Requirements
- Python 3.8+
- Optional: Pillow (for image -> ASCII functionality)

Installation
1. Clone the repository:

   git clone https://github.com/manoj181319/Ascii_art-generator.git
   cd Ascii_art-generator

2. (Optional) Create a virtual environment and install dependencies:

   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt

Usage
- Text to ASCII (example):

  python ascii_art_generator.py --text "Hello" --font standard --output hello.txt

- Image to ASCII (example):

  python ascii_art_generator.py --image input.jpg --width 100 --output art.txt

Note: The exact script and command-line options depend on the implementation in this repository. Replace the script name and options with the ones provided in the project if they differ.

Examples
- Print ASCII art to terminal:

  python ascii_art_generator.py --text "ASCII" --font slant

- Save ASCII art to file:

  python ascii_art_generator.py --image sample.png --width 120 --output sample_ascii.txt

Contributing
Contributions, bug reports, and feature requests are welcome. To contribute:
1. Fork the repository
2. Create a feature branch (git checkout -b my-feature)
3. Commit your changes (git commit -m "Add feature")
4. Push to the branch (git push origin my-feature)
5. Open a pull request describing your changes

License
This project is provided under the MIT License. See LICENSE file for details.

Acknowledgements
- Inspiration from classic ASCII art tools and figlet.
