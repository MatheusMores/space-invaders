import os
import WConio2
import cursor
from colorit import *
from characters import printWithSpecialCharacters

def getPlayerName():
    init_colorit()
    os.system('cls')
    cursor.hide()
    user_name = ''
    while True:
        WConio2.gotoxy(78, 20)
        print(color(("██╗   ██╗ ██████╗███████╗██████╗   ███╗  ██╗ █████╗ ███╗   ███╗███████╗██╗"), Colors.green))
        WConio2.gotoxy(78, 21)
        print(color(("██║   ██║██╔════╝██╔════╝██╔══██╗  ████╗ ██║██╔══██╗████╗ ████║██╔════╝╚═╝"), Colors.green))
        WConio2.gotoxy(78, 22)
        print(color(("██║   ██║╚█████╗ █████╗  ██████╔╝  ██╔██╗██║███████║██╔████╔██║█████╗"), Colors.green))
        WConio2.gotoxy(78, 23)
        print(color(("██║   ██║ ╚═══██╗██╔══╝  ██╔══██╗  ██║╚████║██╔══██║██║╚██╔╝██║██╔══╝"), Colors.green))
        WConio2.gotoxy(78, 24)
        print(color(("╚██████╔╝██████╔╝███████╗██║  ██║  ██║ ╚███║██║  ██║██║ ╚═╝ ██║███████╗██"), Colors.green))
        WConio2.gotoxy(78, 25)
        print(color((" ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝"), Colors.green))


        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()

            if key == 27 or key == 7:
                menu()
            
            if key == 13:
                return user_name
            
            user_name += symbol
            
            printWithSpecialCharacters(user_name, 82, 32)

    

getPlayerName()