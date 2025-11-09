from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

def sketch_effect(pil_img):
    """Apply OpenCV canny edge detection for a better sketch effect"""
    img = np.array(pil_img.convert('L'))
    img_blur = cv2.GaussianBlur(img, (3,3), 0)
    edges = cv2.Canny(img_blur, threshold1=80, threshold2=30)
    sketch = cv2.bitwise_not(edges)
    return Image.fromarray(sketch)

def color_sketch_effect(pil_img, t1=40, t2=120):
    color_np = np.array(pil_img.convert('RGB'))  
    gray_np = cv2.cvtColor(color_np, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(gray_np, (3,3), 0)
    edges = cv2.Canny(img_blur, threshold1=t1, threshold2=t2)
    # Let's make edges black and elsewhere retain the original color
    mask = edges.astype(bool)
    color_sketch = color_np.copy()
    color_sketch[mask] = [0,0,0]  # Draw black lines on color wherever edge found
    return Image.fromarray(color_sketch)


    
    
# --------- USER inputs ---------
output_mode = input("Choose output mode ('bw' for black/white, 'color' for colored ASCII): ").strip().lower()
sketch_mode = input("Choose art style ('normal' or 'sketch'): ").strip().lower()

print("Choose font:")
print("1. Consolas")
print("2. Courier New")
print("3. DejaVuSansMono")
font_choice = input("Enter font number (1/2/3): ").strip()

try:
    font_size = int(input("Font size for output image? (e.g., 12, 16, 20): ").strip())
except:
    font_size = 16
    print("Invalid input. Defaulting font size to 16.")

print("\nThank you! Processing your ASCII art...")

imagePath = 'test.jpg'
image = Image.open(imagePath)
orig_width, orig_height = image.size

if output_mode == "color" and image.mode in ["RGBA", "RGB"]:
    color_ascii = True
    img_for_processing = image.copy()
    print("Processing image in color mode.")
else:
    color_ascii = False
    img_for_processing = image.convert('L')
    print("Processing image in black and white mode.")

# Apply sketch effect if chosen
if sketch_mode == "sketch":
    if color_ascii:
        img_for_processing = color_sketch_effect(img_for_processing)
    else:
        img_for_processing = sketch_effect(img_for_processing)
    print("Applied OpenCV-powered sketch effect.")



#let's determine new dimensions
max_ascii_width = 250
if orig_width > max_ascii_width:
    new_width = max_ascii_width
    new_height = int(orig_height * (new_width / orig_width))
else:
    new_width = orig_width
    new_height = orig_height
    
font_correction = 0.90
new_height = int(new_height * font_correction)
#Image resizing
resized_image = img_for_processing.resize((new_width, new_height))
#Font selection
if font_choice == '1':
    font_path = "fonts/CONSOLA.ttf"
elif font_choice == '2':
    font_path = "fonts/cour.ttf"
elif font_choice == '3':
    font_path = "fonts/DejaVuSansMono.ttf"

font = ImageFont.truetype(font_path, size=font_size)    

# [0 = black][255 = white]
ASCII_CHARS = "@%#*+=-:. "

if color_ascii:
    #colored ascii
    pixels = resized_image.load()
    ascii_lines = []

    for y in range(resized_image.height):
        line_chars = []
        for x in range(resized_image.width):
            r, g, b = pixels[x, y][:3]
            value = int((r + g + b) / 3)
            #Scale pixel value (0-255) to match our ASCII_CHARS length
            char = ASCII_CHARS[value * (len(ASCII_CHARS) - 1) // 255]
            line_chars.append((char, (r, g, b)))
        ascii_lines.append(line_chars)

    # render
    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    img_width = char_width * resized_image.width
    img_height = char_height * resized_image.height
    ascii_image = Image.new("RGB", (img_width, img_height), color=(255,255,255))
    draw = ImageDraw.Draw(ascii_image)

    for j, line in enumerate(ascii_lines):
        for i, (char, color) in enumerate(line):
            draw.text((i * char_width, j * char_height), char, fill=color, font=font)
    ascii_image.save("output_asciiart.jpg")
    print("Color ASCII art has been saved as output_asciiart.jpg")
else:
    #Ascii grayscale conversion and rendering code
    pixels = resized_image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        index = pixel_value * (len(ASCII_CHARS) - 1) // 255
        ascii_str += ASCII_CHARS[index]
    #Arrange the Ascii string into lines (rows)
    ascii_art = ""
    for i in range(0, len(ascii_str), resized_image.width):
        ascii_art += ascii_str[i:i+resized_image.width] + "\n"

    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    img_width = char_width * resized_image.width
    img_height = char_height * resized_image.height
    ascii_image = Image.new("L", (img_width, img_height), color=255)
    draw = ImageDraw.Draw(ascii_image)
    for j, line in enumerate(ascii_art.splitlines()):
        draw.text((0, j * char_height), line, fill=0, font=font)
    ascii_image.save("output_asciiart.jpg")
    print("B/W ASCII art has been saved as output_asciiart.jpg")
