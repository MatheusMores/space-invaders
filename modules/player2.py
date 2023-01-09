from colorit import *
import cursor
import os
import WConio2

character = "§"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
gray = color(character, (180,180,180))
dark_gray = color(character, (125, 125, 125))
light_gray = color(character, (225,225,225))


class Player2:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y

        self.matrizPlayer = [
            [None, None, None, None, None, None, light_gray, None, None, None, None, None, None],
            [None, None, None, None, None, light_gray, light_gray, light_gray, None, None, None, None, None],
            [None, None, None, None, light_gray, light_gray, blue, light_gray, light_gray, None, None, None, None],
            [None, None, None, light_gray, light_gray, blue, blue, blue, light_gray, light_gray, None, None, None],
            [None, gray, light_gray, light_gray, light_gray, gray, gray, gray, light_gray, light_gray, light_gray, gray, None],
            [gray, light_gray, light_gray, light_gray, light_gray, dark_gray, red, dark_gray, light_gray, light_gray, light_gray, light_gray, gray],
            [gray, light_gray, light_gray, None, None, yellow, red, yellow, None, None, light_gray, light_gray, gray],
            [dark_gray, gray, None, None, None, None, yellow, None, None, None, None, gray, dark_gray]
        ]
        
    def controll(self, count):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
    
            if symbol == 'a':
                if count%3 == 0:
                    self.x-=1
    
            if symbol == 'd':
                if count%3 == 0:
                    self.x+=1
            



