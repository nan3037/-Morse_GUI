import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
myled = LED(18)

mywin = Tk()
mywin.title("Morse Code GUI")
myFont = tkinter.font.Font(family = "Georgia", size = 22, weight = "bold")
inputFont = tkinter.font.Font(family = "Arial", size = 16)
mywin.minsize(540, 420)
mywin.configure(bg = "white")

def dot():
    myled.on()
    time.sleep(0.5)
    myled.off()
    time.sleep(0.15)
    
def dash():
    myled.on()
    time.sleep(1.5)
    myled.off()
    time.sleep(0.15)
    
def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dot()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dot()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()
    
def g():
    dot()
    dot()
    dash()

def h():
    dot()
    dot()
    dot()
    dot()
    
def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()
    
def k():
    dash()
    dot()
    dash()
    
def l():
    dot()
    dash()
    dot()
    dot()
    
def m():
    dash()
    dash()
    
def n():
    dash()
    dot()
    
def o():
    dash()
    dash()
    dash()
    
def p():
    dot()
    dash()
    dash()
    dot()
    
def q():
    dash()
    dash()
    dot()
    dash()
    
def r():
    dot()
    dash()
    dot()
    
def s():
    dot()
    dot()
    dot()
    
def t():
    dash()
    
def u():
    dot()
    dot()
    dash()
    
def v():
    dot()
    dot()
    dot()
    dash()
    
def w():
    dot()
    dash()
    dash()    

def x():
    dash()
    dot()
    dot()
    dash()
    
def y():
    dash()
    dot()
    dash()
    dash()
    
def z():
    dash()
    dash()
    dot()
    dot()
    
       
def ledSwitch():
    
    blinkText = codeText.get() #range set upto 13 hence it would take values up until 12 characters
    
    for letter in blinkText:
        print(letter, " ")
        if letter == "a":
            a()
        elif letter == "b":
            b()
        elif letter == "c":
            c()
        elif letter == "d":
            d()
        elif letter == "e":
            e()
        elif letter == "f":
            f()
        elif letter == "g":
            g()
        elif letter == "h":
            h()
        elif letter == "i":
            i()
        elif letter == "j":
            j()
        elif letter == "k":
            k()
        elif letter == "l":
            l()
        elif letter == "m":
            m()
            
        elif letter == "n":
            n()
        elif letter == "o":
            o()
        elif letter == "p":
            p()
        elif letter == "q":
            q()
        elif letter == "r":
            r()
        elif letter == "s":
            s()
        elif letter == "t":
            t()
        elif letter == "u":
            u()
        elif letter == "v":
            v()
        elif letter == "w":
            w()
        elif letter == "x":
            x()
        elif letter == "y":
            y()
        elif letter == "z":
            z()
        time.sleep(3.5)

codeText = Entry(mywin, width=12, font = inputFont)
codeText.grid(row = 3, column = 50)
codeText.grid(padx = 20,pady = 20)
    
button= Button(mywin, text = "Start Blinking", font = myFont, command = ledSwitch, bg = "blue" , height = 2, width = 10)
button.grid(row = 5, column = 50)
codeText.grid(padx = 20, pady =20)

  
