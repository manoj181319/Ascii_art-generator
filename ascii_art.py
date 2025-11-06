from PIL import Image, ImageDraw, ImageFont

imagePath = 'test.jpg'
image = Image.open(imagePath)
#let's determine new dimensions
new_width = 100
width, height = image.size
aspect_ratio = height / width
new_height = int(aspect_ratio * new_width)
#let's resize the image
resized_image = image.resize((new_width, new_height))
#let's convert to grayscale for better image production
gray_image = resized_image.convert('L')
gray_image.save('gray_sample.jpg')
gray_image.show()
# [0 = black][255 = white]
ASCII_CHARS = "@%#*+=-:. "
pixels = gray_image.getdata() #give pixel values as a list

ascii_str = ""
for pixel_value in pixels:
    # Scale pixel value (0-255) to match our ASCII_CHARS length
    index = pixel_value * (len(ASCII_CHARS) - 1) // 255
    ascii_str += ASCII_CHARS[index]
    
# Arrange the Ascii string into lines (rows)
ascii_art = ""
for i in range(0, len(ascii_str), new_width):
    ascii_art += ascii_str[i:i+new_width] +"\n"

# Print result to console    
print(ascii_art)

font = ImageFont.load_default()
char_width, char_height = font.getsize("A")
img_width = char_width * new_width
img_height = char_height * new_height

ascii_image = Image.new("L", (img_width, img_height), color=255)
draw = ImageDraw.Draw(ascii_image)

for j, line in enumerate(ascii_art.splitlines()):
    draw.text((0,j * char_height), line, fill=0, font=font)

ascii_image.save("output_asciiart.jpg")
print("ASCII art has been saved as output_asciiart.jpg")