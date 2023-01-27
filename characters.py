import WConio2
from colorit import *

characters = [
    {"letra": "a",
    "special": [
        '█▀▀█',
        '█▄▄█' ,
        '▀  ▀'
    ]},
    {"letra": "b",
    "special": [
        '█▀▀▄',
        '█▀▀▄',
        '▀▀▀'
    ]},
    {"letra": "c",
    "special": [
        '█▀▀',
        '█' ,
        '▀▀▀'
    ]},
    {"letra": "d",
    "special": [
        '█▀▀▄',
        '█  █',
        '▀▀▀'
    ]},
    {"letra": "e",
    "special": [
        '█▀▀',
        '█▀▀',
        '▀▀▀'
    ]},
    {"letra": "f",
    "special": [  
        '█▀▀',
        '█▀▀',
        '▀'
    ]},
    {"letra": "g",
    "special": [
        '█▀▀▀', 
        '█ ▀█',
        '▀▀▀▀'
    ]},
    {"letra": "h",
    "special": [
        '█  █',
        '█▀▀█',
        '▀  ▀'
    ]},
    {"letra": "i",
    "special": [
        ' ▀ ',
        '▀█▀',
        '▀▀▀'
    ]},
    {"letra": "j",
    "special": [
        '  ▀',
        '  █',
        '█▄█'
    ]},
    {"letra": "k",
    "special": [
        '█ █', 
        '█▀▄', 
        '▀ ▀'
    ]},
    {"letra": "l",
    "special": [
        '█  ' ,
        '█  ' ,
        '▀▀▀'
    ]},
    {"letra": "m",
    "special": [
        '█▀▄▀█ ', 
        '█ ▀ █ ', 
        '▀   ▀ '
    ]},
    {"letra": "n",
    "special": [
        '█▀▀▄', 
        '█  █' ,
        '▀  ▀'   
    ]},
    {"letra": "o",
    "special": [
        '█▀▀█',
        '█  █',
        '▀▀▀▀'
    ]},
    {"letra": "p",
    "special": [
        '█▀▀█',
        '█  █',
        '█▀▀▀'
    ]},
    {"letra": "q",
    "special": [
        '█▀▀█',
        '█  █',
        '▀▀▀█'
    ]},
    {"letra": "r",
    "special": [
        '█▀▀█', 
        '█▄▄▀', 
        '▀ ▀▀'
    ]},
    {"letra": "s",
    "special": [
        '█▀▀', 
        '▀▀█',
        '▀▀▀'
    ]},
    {"letra": "t",
    "special": [
        '▀█▀' ,
        ' █ ' ,
        ' ▀ '
    ]},
    {"letra": "u",
    "special": [
        '█  █',
        '█  █', 
        ' ▀▀▀'
    ]},
    {"letra": "v",
    "special": [
        '▀█ █▀', 
        ' █▄█ ', 
        '  ▀  '
    ]},
    {"letra": "w",
    "special": [
        '█   █', 
        '█▄█▄█', 
        ' ▀ ▀ '
    ]},
    {"letra": "x",
    "special": [
        '█ █', 
        '▄▀▄',
        '▀ ▀'  
    ]},
    {"letra": "y",
    "special": [
        '█  █', 
        '█▄▄█', 
        '▄▄▄█'
    ]},
    {"letra": "z",
    "special": [
        '▀▀█',
        '▄▀ ', 
        '▀▀▀'
    ]},
    {"letra": " ",
    "special": [
        '   ',
        '   ', 
        '   '
    ]},
    {"letra": "1",
    "special": [
        '▄█',
        ' █' ,
        '▄█▄'
    ]},
    {"letra": "2",
    "special": [
        '█▀█',
        ' ▄▀',
        '█▄▄'
    ]},
    {"letra": "3",
    "special": [
        '█▀▀█', 
        '  ▀▄', 
        '█▄▄█'
    ]},
    {"letra": "4",
    "special": [
        ' █▀█ ',
        '█▄▄█▄', 
        '   █ '
    ]},
    {"letra": "5",
    "special": [
        '█▀▀',
        '▀▀▄',
        '▄▄▀'
    ]},
    {"letra": "6",
    "special": [
        '▄▀▀▄', 
        '█▄▄ ', 
        '▀▄▄▀'
    ]},
    {"letra": "7",
    "special": [
        '▀▀▀█', 
        '  █ ' ,
        ' ▐▌ '
    ]},
    {"letra": "8",
    "special": [
        '▄▀▀▄', 
        '▄▀▀▄', 
        '▀▄▄▀'
    ]},
    {"letra": "9",
    "special": [
        '▄▀▀▄', 
        '▀▄▄█', 
        ' ▄▄▀'
    ]},
    {"letra": "0",
    "special": [
        '█▀▀█', 
        '█▄▀█', 
        '█▄▄█'
    ]},
    {"letra": "_",
    "special": [
        '   ', 
        '   ', 
        '▄▄▄▄'
    ]},
    {"letra": "-",
    "special": [
        '   ', 
        '▄▄▄', 
        '   '
    ]},
    {"letra": ":",
    "special": [
        '▄', 
        ' ',
        '▀'
    ]},
]

def printWithSpecialCharacters(palavra, x, y):
    x_counter = 0
    palavra = palavra.lower()
    
    for letra_nome in palavra:
        for character in characters:
            if letra_nome == character["letra"]:
                WConio2.gotoxy(x + x_counter, y)
                print(color((character["special"][0]), Colors.green))
                WConio2.gotoxy(x + x_counter, y + 1)
                print(color((character["special"][1]), Colors.green))
                WConio2.gotoxy(x + x_counter, y + 2)
                print(color((character["special"][2]), Colors.green))
                
                x_counter += 5
