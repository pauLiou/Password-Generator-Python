import main
import PySimpleGUI as sg
from pyperclip import copy

font = 'Courier_New'

sg.theme('DarkBlue')
layout = [
    [sg.Text("Please Enter Your Username: ",font = font),sg.InputText(key='name',font=font)],
    [sg.Text("Length of Password:",font = font),sg.Slider(range = (5,50),
                                                orientation = 'horizontal',
                                                key='passlen',
                                                default_value = 20,
                                                font=font)],
    [sg.Submit(font=font),sg.Cancel(font=font)],
    [sg.Text(size=(50,1), key = '-OUTPUT0-',visible = False,font=font)],
    [sg.Text(size=(50,1), key = '-OUTPUT1-',visible = False,font=font)],
    [sg.Text(size=(50,1), key = '-OUTPUT2-',visible = False,font=font,text_color= 'green2')],
    [sg.Button('Copy to Clipboard',key = '_1_',visible = False,font=font)]
    ]

window = sg.Window("Password Generator",layout)

while True:
    event, values = window.read()

    if event == "Submit":
        Person = main.User(values['name'],[])
        Person.passGen(int(values['passlen']))
        window['-OUTPUT0-'].update('Username: ' + str(Person.name),visible = True)
        window['-OUTPUT1-'].update('Generated password: ',visible = True)
        window['-OUTPUT2-'].update(Person.password,visible = True)
        window['_1_'].update(visible = True)

    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    if event == '_1_':
        copy(Person.password)

window.close()

