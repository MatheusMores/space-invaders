import os
import cursor
import WConio2
from colorit import *
from logo import printLogo


from modules.player import Player
from modules.enemy import Enemy
from modules.printTela import printTela

player_x = 30
player_y = 40

def menu():
    init_colorit()
    os.system('cls')
    cursor.hide()
    while True:
        printLogo(14, 2)

        a = int(input())
        if (a == 1):
            iniciarJogo()



def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()

    player = Player(player_x, player_y)
    enemys = []
    enemy1 = Enemy(20, 10)
    enemy2 = Enemy(40, 10)

    enemys.append(enemy1)
    enemys.append(enemy2)

    while True:

        printTela(player.pontuacao)

        enemy1.printEnemy()

        enemy2.printEnemy()

        player.shoot(enemys)

        player.printPlayer()

        player.controll()

menu()
