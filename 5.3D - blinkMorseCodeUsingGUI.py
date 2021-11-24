##
#    Embedded Systems Development
#    Exercise : Task 5.3D - Blink Morse Code Using GUI
#    Name : Ereena Bagga
#    Student ID : 2010993040
##

from tkinter import *
import tkinter.font as FONT
import RPi.GPIO as GPIO
from gpiozero import LED
import time

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# GUI Defintions
win = Tk()
win.title("BLINK MORSE CODE")
myFont = FONT.Font(family = 'Helvetica', size = 14, weight = 'bold')

# LED Pin Definition
led = LED(12)

# Declare input string to be translated into morse code
inputString = StringVar()

# Declare duration for dot as 1 second
dotDuration = 1

# Declare duration for dash as 3*dotDuration, i.e., 3 seconds
dashDuration = dotDuration * 3

# List for letters 'A' to 'Z' in morse code
letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
  ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
  "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

# List for numbers 0 to 9 in morse code
numbers = ["-----", ".----", "..---", "...--", "....-", ".....", "-....",
  "--...", "---..", "----."]

# Event Functions

# This method flashes the morse code for the input letter or number
def blinkMorseCode(morseCode):
    
  # Iterating through the entire string of morse code
  for char in morseCode:
    # Turn on the LED
    led.on()

    # If the given character is a dot
    if (char == '.'):
      # Give a delay for 1 second
      time.sleep(dotDuration)

    # Else if the given character is a dash
    else:
      # Give a delay for 3 seconds
      time.sleep(dashDuration)

    # Turn the led off
    led.off()

    # A delay of 1 second is given after blinking each part of a character
    time.sleep(dotDuration)

  # A delay of 3 seconds is given after blinking each character
  time.sleep(dashDuration)

# This method translates the input string into morse code
def translateMorseCode():
    
    inputString = morseCode.get()
    
    # Print Input
    print("INPUT:")
    
    # Counter variable
    i = 1
    
    for c in inputString:
        
        # Translation will be done for a maximum of 12 characters
        if (i > 12):
          break
        
        print(c, end= " ")
        
        # If the input given belongs to uppercase letters
        if (c >= 'A' and c <= 'Z'):
          # Method call to blink morse code on LED
          blinkMorseCode(letters[ord(c) - ord('A')]) 

        # If the input given belongs to lowercase letters
        elif (c >= 'a' and c <= 'z'):
          # Method call to blink morse code on LED
          blinkMorseCode(letters[ord(c) - ord('a')]) 

        # If the input given belongs to numbers
        elif (c >= '0' and c <= '9'):
          # Method call to blink morse code on LED
          blinkMorseCode(numbers[ord(c) - ord('0')]) 

        # If the input given is a space between words
        elif (c == ' '):
          # Give a delay equal to seven dots for space
          time.sleep(dotDuration * 7)
          
        i+=1
    
# This method destroys the window and sets the GPIO pins back to their intial settings
def close():
    GPIO.cleanup()
    win.destroy()

# Widgets
morseCode = Entry(win, font = myFont, width = 30)
morseCode.grid(row = 0, column = 0)

morseCodeButton = Button(win, text = 'LOAD MORSE CODE', font = myFont, command = translateMorseCode, bg = 'bisque2', height = 2, width = 30)
morseCodeButton.grid(row = 0, column = 1)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'red', height = 2, width = 15)
exitButton.grid(row = 1, column = 1)

win.protocol("WM_DELETE_WINDOW",close) # exit cleanly

win.mainloop() # loop forever