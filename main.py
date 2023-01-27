import os
import cursor
from colorit import *

import WConio2
from printTela import printTela
from player import Player
from enemy import Enemy
from menu import Menu
from Highscore import Highscores

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
    os.system('cls')
    while True:
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()

            if key == 27:
                menu()

        highs = Highscores() 
        highs.printHighScore()

def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()

    player = Player('Jose')
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
        player.printVidas()

        player.controll()

menu()
