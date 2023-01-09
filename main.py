import os
import cursor
import WConio2
from colorit import *

from modules.player import Player


def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()
    blue = color('#', (0, 106, 255))

    player_x = 150
    player_y = 40
    counterX, counterY = 0, 0
    count, countY = 0, 0


    player = Player(player_x, player_y)
    
    while True:
        WConio2.gotoxy(0, 0)
    
        # Bordas de cima
        print(blue * 237)

        counterY = 0
        for j in range(64):
            print(blue,end="")
            
            counterX = 0

            for k in range(235):
                char = " "

                countY = player.gravity(countY)

                player.controll(count)

                if (k < 22 + player.x and j < 19 + player.y):
                    if k == player.x + counterX and j == player.y + counterY:
                        if player.matrizPlayer[counterY][counterX] != None:
                            char = player.matrizPlayer[counterY][counterX]
                        
                        counterX+=1
                        
                
                print(char, end="")
            
            if j >= player.y:
                counterY += 1
            
            print(blue)

        # Bordas de baixo 
        print(blue * 237)

        count += 1
        countY += 1

    
        

iniciarJogo()