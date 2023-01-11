import os
import cursor
import WConio2
from colorit import *

from modules.player2 import Player2

MAIN_X = 32
MAIN_Y = 0
player_x = 30
player_y = 31


def iniciarJogo():
    counterX, counterY = 0, 0
    contador_velocidade = 0
    init_colorit()
    os.system('cls')
    cursor.hide()

    player = Player2(player_x, player_y)

    while True:
        WConio2.gotoxy(0, 0)

        print('#' * 101)

        counterY = 0
        for j in range(40):
            character = ''
            #print('#',end="")
            character += "#"
            counterX = 0

            for i in range(99):

                char = " "

                player.controll(contador_velocidade)

                if (i < 13 + player.x and j < 8 + player.y):
                    if i == player.x + counterX and j == player.y + counterY:
                        if player.matrizPlayer[counterY][counterX] != None:
                            char = player.matrizPlayer[counterY][counterX]
                        
                        counterX+=1
                        
            
                character += char

            if j >= player.y:
                counterY += 1
            
            character +="#"
            print(character)

        print("#" * 101)
        
        contador_velocidade += 1



iniciarJogo()

