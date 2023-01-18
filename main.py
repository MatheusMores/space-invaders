import os
import cursor
import WConio2
from colorit import *

from modules.player import Player
from modules.enemy import Enemy
from modules.printTela import printTela

player_x = 30
player_y = 40

def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()

    player1 = Player(player_x, player_y)
    enemys = []
    enemy1 = Enemy(20, 10)
    enemy2 = Enemy(40, 10)

    enemys.append(enemy1)
    enemys.append(enemy2)

    while True:

        printTela()
        
        enemy1.printEnemy()

        enemy2.printEnemy()


        print(player1.shoot(enemys))

        player1.printPlayer()

        player1.controll()


iniciarJogo()
