# Nokia LCD
==========

## Description
----------------
Raspberry Pi Python library for the using the PCD8544 LCD (Nokia 5110/3310) Hat / Shields.
This works off the shelf for Sunflower Hat / Shield, but it can be easily configured to be used with other PCD8544's.

This was reforged by Kabe for SourcExplained and was heavily based on:
 - [Tony DiCola from Adafruit](https://github.com/adafruit/Adafruit-PCD8544-Nokia-5110-LCD-library)
 - [Xavier Berger](https://github.com/XavierBerger/pcd8544)
   
The goal was to merges both libraries, and add the flexibility of Tony's lib, with the ability to simple write text of Xavier's lib. This library, and all its content including all all text are covered by the MIT license.  

## Dependencies
----------------
This library depends on the following other libraries:
 - [Adafruit Python GPIO Library](https://github.com/adafruit/Adafruit_Python_GPIO)
 - [Python Imaging Library](https://pypi.python.org/pypi/PIL)
    
## Using it
----------------
How to use this library:
Update the list of available packages and their version
`sudo apt-get update`

Check if installed packages are up to date and upgrade them if needed
`sudo apt-get upgrade`

Install python dev + setuptools + git + pip + pil 
`sudo apt-get install python-dev python-setuptools git python-pip python-imaging`

Install python libraries
`sudo pip install RPi.GPIO Adafruit_BBIO`

Now to download and install the Nokia LCD python library code and examples, execute the following commands:

`git clone https://github.com/sourcexplained/NokiaLCD.git
cd NokiaLCD
sudo python setup.py install`

Test the sample files
`cd examples`

If you using the SunFounder Raspberry Pi Display Mini LCD 84*48 PCD8544 Shield For Model B+/B
[Product Page](http://www.sunfounder.com/index.php?c=show&id=66&model=PCD8544%20Mini%20LCD)
The Pinouts should work of the shelf, and you can skip the file editing 
  SCLK = 17 | DIN = 18 | DC = 27 | RST = 23 | CS = 22 

 If not, please change the example class initialization 
from:
`   disp = NokiaLCD(27, 23, 17, 18, 22) or disp = NokiaLCD()`
to:
`   disp = NokiaLCD( DC_pin, RST_pin, SCLK_pin, DIN_pin, CS_pin)`
where the *_pin you can find in your spec/datasheet   

to edit the files use 

`nano <example_filename.py>`

edit the files according to the description above, and exit and save by pressing 

Ctrl+X and then Y (N will exit without saving)

to run a example 
`sudo python ./<example_filename.py>`

and you should see your LCD screen showing something
