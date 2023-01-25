from msilib.schema import Error
import WConio2

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
]

def printWithSpecialCharacters(x, y):
    nome = input("nome: ").lower()
    x_counter = 0
    
    for letra_nome in nome:
        for character in characters:
            if letra_nome == character["letra"]:
                WConio2.gotoxy(x + x_counter, y)
                print(character["special"][0])
                WConio2.gotoxy(x + x_counter, y + 1)
                print(character["special"][1])
                WConio2.gotoxy(x + x_counter, y + 2)
                print(character["special"][2])
                
                x_counter += len(character["special"]) + 3
        

printWithSpecialCharacters(20, 20)