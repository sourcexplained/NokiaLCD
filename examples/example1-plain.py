#!/usr/bin/python

#
# Example of NokiaLCD lib
#
# by Kabe for SourcExplained
#
# Boot - Text, load image, custom patterns
#


from NokiaLCD import NokiaLCD
import time

# The default pins are NokiaLCD(27, 23, 17, 18, 22)
# For Sunfounder Raspberry Pi Hat but is valid for other
# change according to your scheme/specifications
disp = NokiaLCD(27, 23, 17, 18, 22)
# Initialize library 
disp.begin(contrast=60) # will show Raspberry Pi Logo
time.sleep(.25)

# Clear screen
disp.clear()
time.sleep(.1)
# Display Text
disp.text("This is a test")
time.sleep(.2)
disp.text("4 Raspberry Pi")
time.sleep(.2)	
disp.text("Nokia PCD8544 ")
time.sleep(.2)	
disp.text("Hello", row = 5, align = NokiaLCD.AlignLeft)
disp.text("World", row = 5, align = NokiaLCD.AlignRight)
time.sleep(1)	

# Load Image code is commented because (you must have an image file)
disp.load_image('happycat.png')
time.sleep(1)

# Display Raspberry Pi Logo (using a byte array)
disp.data(disp.LOGO_RPI)
time.sleep(1)

# position system to write text
disp.gotoxy(0,4)
disp.text('By')
disp.data_char(':') # or single character

# you can define your own patterns|characters by 
# passing to data_char arrays of bytes 
# to maintain character alignment the num bytes should be multiple of 6
#
# 0, 0x04 = 00001000
# 1, 0x08 = 00010000
# 2, 0x10 = 00100000
# 3, 0x20 = 01000000
# 4, 0x10 = 00100000
# 5, 0x08 = 00010000
#
# Note that this will show rotated on screen 

pattern = [0x04, 0x08, 0x10, 0x20, 0x10, 0x08]
for i in range(NokiaLCD.NColumns - 3): 
    for j in range(6):
        disp.data_char([ pattern[j] ])
        time.sleep(.05)	

disp.gotoxy(0,5)
disp.text("SourcExplained")
