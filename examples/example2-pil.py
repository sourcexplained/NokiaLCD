#!/usr/bin/python

#
# Example of NokiaLCD lib
#
# by Kabe for SourcExplained
#
# Boot - Text, load image, custom patterns
#

# The default pins are NokiaLCD(27, 23, 17, 18, 22)
# For Sunfounder Raspberry Pi Hat but is valid for other
# change according to your scheme/specifications
# Create blank image for drawing.

from NokiaLCD import NokiaLCD
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
from random import randrange

disp = NokiaLCD(27, 23, 17, 18, 22)
# Initialize library 
disp.begin(contrast=60) # will show Raspberry Pi Logo
disp.clear()

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (NokiaLCD.Width, NokiaLCD.Height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,NokiaLCD.Width,NokiaLCD.Width), outline=255, fill=255)

# Draw some shapes.
draw.ellipse((2,2,22,22), outline=0, fill=255)
draw.rectangle((24,2,44,22), outline=0, fill=255)
draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
# update screen
disp.image(image)
time.sleep(.5)

for i in range(10):
  x1 = randrange(NokiaLCD.Width)
  y1 = randrange(NokiaLCD.Height / 2)
  x2 = randrange(NokiaLCD.Width)
  y2 = randrange(NokiaLCD.Height / 2)
  draw.line((x1,y1,x2,y2), fill=0)

# update screen
disp.image(image)
time.sleep(.5)

# Load default font.
font = ImageFont.load_default()
# Write some text.
draw.text((8,34), 'Hello World!', font=font)
# Display image.
disp.image(image)
