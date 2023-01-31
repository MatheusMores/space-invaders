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
    
    enemy1 = Enemy(10, 7)
    enemy2 = Enemy(30, 7)
    enemy3 = Enemy(50, 7)
    enemy4 = Enemy(70, 7)
    enemy5 = Enemy(90, 7)
    enemy6 = Enemy(110, 7)
    enemy7 = Enemy(130, 7)
    # enemy8 = Enemy(150, 7)
    # enemy9 = Enemy(170, 7)
    # enemy10 = Enemy(190, 7)

    enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]


    while True:

        printTela(player.pontuacao)

        enemy1.iniciarJogo(enemies, player)
        enemy2.iniciarJogo(enemies, player)
        enemy3.iniciarJogo(enemies, player)
        enemy4.iniciarJogo(enemies, player)
        enemy5.iniciarJogo(enemies, player)
        enemy6.iniciarJogo(enemies, player)
        enemy7.iniciarJogo(enemies, player)
        # enemy8.iniciarJogo(enemies, player)
        # enemy9.iniciarJogo(enemies, player)
        # enemy10.iniciarJogo(enemies, player)

        #conferirNumeroInimigos()


        player.shoot(enemies)

        player.printPlayer()
        player.printVidas()

        player.controll()

menu()
