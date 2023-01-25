import os
import cursor
import WConio2
from colorit import *

from modules.printTela import printTela
from modules.player import Player
from modules.enemy import Enemy
from menu import Menu

player_x = 30
player_y = 40

def menu():
    init_colorit()
    os.system('cls')
    cursor.hide()
    menu = Menu()

    while True:
        menu.printMenu()
        opcao = menu.selectOpcao()

        if opcao == 0:
            iniciarJogo()
        
        elif opcao == 1:
            printHighscores()

def printHighscores():
    pass

def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()

    player = Player('Jose', player_x, player_y)
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
