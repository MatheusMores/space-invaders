import os
import cursor
import WConio2
from colorit import *

from modules.player import Player
from modules.printTela import printTela

player_x = 30
player_y = 40
cont = 0

def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()

    player1 = Player(player_x, player_y)


    while True:
        printTela()
        player1.printPlayer()

        player1.controll(cont)
    
        

        



iniciarJogo()