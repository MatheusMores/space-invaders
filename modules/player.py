from colorit import *
import cursor
import os
import WConio2

from .limiteTela import LimiteTela

init_colorit()
os.system('cls')
cursor.hide()


character = "§"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
white = color(character, Colors.white)

class Player:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y

        self.matrizPlayer = [
            [None, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, None, blue, blue, blue, blue, blue, blue, None, None, None, None, blue, blue, blue, blue, blue, blue, blue, None, None, None],
            [None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, None, None, None, None, None, None, blue, blue, blue, blue, blue],
            [None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, white],
        ]
    
    def controll(self, count):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
    
            if symbol == 'a':
                if LimiteTela.limitePlayerX(self.x - 1) == False:
                    pass
                elif count%2 == 0:
                    self.x-=1
    
            if symbol == 'd':
                if LimiteTela.limitePlayerX(self.x + 1) == False:
                    pass
                elif count%2 == 0:
                    self.x+=1
            
            if symbol == ' ':
                if LimiteTela.limitePlayerY(self.y - 1) == False:
                    pass
                elif count%5 == 0:
                    self.y-=2
                    


    def gravity(self, countY):   
        if LimiteTela.limitePlayerY(self.y + 1) != False:
            if countY%2 == 0 and countY != 0:
                self.y+=1
                return 3
        
        return countY


    

    