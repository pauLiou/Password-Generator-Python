import string
from string import ascii_uppercase, digits, printable
import random
from random import choice, shuffle
import PySimpleGUI as sg


# we are going to create a simple program that can create a password for the user with a small interface
class User:
    def __init__(self,name,password):
        self.name = name # the user will input a username and get a password generated for them
        self.password = password # the password will be stored within the class here
        
    def passGen(self,passlen):
        self.password = ''.join(choice(
            printable[0:68]) for i in range(
                passlen)) # string of random characters, symbols, and numbers at the length specified
        self.password = self.password[:-2]
        self.password += (choice(ascii_uppercase)) # add at least 1 capital letter
        self.password += (choice(digits)) # add at least 1 digit
        return shuffle(list(self.password))

sg.theme('DarkBlue')
layout = [
    [sg.Text("Please Enter Your Username: "),sg.InputText()],
    [sg.Text("Length of Password:"),sg.Slider(range = (5,50),
                                                orientation = 'horizontal',
                                                key='passlen',
                                                default_value = 20)],
    [sg.Submit(),sg.Cancel()]
    ]

window = sg.Window("Password Generator",layout)

while True:
    event, vaues = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()





