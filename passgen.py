# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated 
# password to clipboard
import pyperclip

# random module will be used in generating the random password
import random

# initializing the tkinter
root = Tk()

# setting the width and height of the gui
root.geometry("400x400")    # x is small case here

# declaring a variable of string type and this variable will be 
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to 
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
