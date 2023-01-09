from colorit import *
import cursor
import os
import WConio2

character = "§"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
gray = color(character, (55,54,51))
dark_gray = color(character, (25,25,25))
light_gray = color(character, (200,200,200))



class Player2:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y

        self.matrizPlayer = [

            [None, dark_gray, light_gray, gray, gray, dark_gray, None, None, None, None, dark_gray, gray, gray, light_gray, dark_gray, None],
            [gray, light_gray, gray, gray, gray, None, None, None,  None, None, None, gray, gray, gray, light_gray, gray],
            [gray, light_gray, light_gray, gray, None, None, None, None, None, None, None, None, gray, light_gray, light_gray, gray],
            [gray, None, dark_gray, dark_gray, None, None, None, None, None, None, None, None, dark_gray, dark_gray, None, gray],
            [None, None, red, red, None, None, None, None, None, None, None, None, red, red, None, None, None]
        ]

    def printPlayer(self):
        counter = 0
        WConio2.gotoxy(self.x, self.y)
        for x in self.matrizPlayer:
            WConio2.gotoxy(self.x, self.y + counter)
            for y in x:
                if (y == None):
                    print(' ', end="")
                else:
                    print(y, end="")
            print('')
            counter +=1

p1 = Player2(1, 2)
p1.printPlayer()

