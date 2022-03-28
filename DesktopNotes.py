import pyautogui
import ctypes
import os
import sys
from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk  # Python 3
import keyboard
import time
from tkinter import filedialog

## Hide Tkinter window
root = Tk()
root.withdraw()

## Get Screen Width and Height
sWidth, sHeight = pyautogui.size()

print('\n'*2)
print("'alt + ctrl + shift + n'" + " to set clipboard to wallpaper")
print('\n'*2)
print("'alt + ctrl + shift + k'" + " to exit")
print('\n'*2)

## Popup Windows File Chooser
print("Choose Background Image")
file_path1name = filedialog.askopenfilename(title="Choose Targets File")

## Pull in fresh background
bgImage = Image.open(file_path1name)

## Set Fresh Background
bgImage.save(file_path1name + "_tmp.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path1name + "_tmp.jpg" , 0)

## Set Font
font = ImageFont.truetype('Excluded.ttf',24)

## Make Background Image Editable
imageEditable = ImageDraw.Draw(bgImage)

## FUNCTIONS ##
def set_wallpaper():
    ## get Clipboard and put it in titleText variable
    titleText = Tk().clipboard_get()
    
    ## Jank attempt for multi monitor support
    ## It works as long as all monitors are the same rsolution
    tmpX, tmpY = pyautogui.position()
    if(tmpX > sWidth):
        tmpX = tmpX - sWidth
    elif(tmpX < 0):
        tmpX = tmpX + sWidth
    if(tmpY > sHeight):
        tmpY = tmpY - sHeight
    elif(tmpY < 0):
        tmpY = tmpY + sHeight
    
    ## Set the text onto the imageEditable variable and save the update to _tmp.jpg and then actually set the background to _tmp.jpg
    imageEditable.text((tmpX,tmpY), titleText, (237, 230, 211), font = font)
    bgImage.save(file_path1name + "_tmp.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path1name + "_tmp.jpg" , 0)
 
 ## Say a nice good bye message and set the desktop back to the clean version of the desktop
def cleanup():
    print("Good Bye")
    os.remove(file_path1name + "_tmp.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path1name, 0)

## Get HotKey and Run Set_Wallpaper()
keyboard.add_hotkey('alt + ctrl + shift + n', set_wallpaper, args=())
  
## Break out of the program on this hotkey
keyboard.wait('alt + ctrl + shift + k')
cleanup()