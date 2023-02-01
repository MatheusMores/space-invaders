import os
import cursor
from colorit import *

import WConio2
from characters import printWithSpecialCharacters
from conferirNumeroInimigos import conferirNumeroInimigos
from limiteTela import CONST_X
from printTela import printTela
from player import Player
from enemy import Enemy
from menu import Menu
from highscore import Highscores

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

            if key == 27 or key == 7:
                menu()

        Highscores.printHighScore()

def gameOver(pontuacao):
    init_colorit()
    os.system('cls')
    cursor.hide()
    while True:
        WConio2.gotoxy(82, 20)
        print(color((' ██████╗  █████╗ ███╗   ███╗███████╗   █████╗ ██╗   ██╗███████╗██████╗'), Colors.green))
        WConio2.gotoxy(82, 21)
        print(color(('██╔════╝ ██╔══██╗████╗ ████║██╔════╝  ██╔══██╗██║   ██║██╔════╝██╔══██╗'), Colors.green))
        WConio2.gotoxy(82, 22)
        print(color(('██║  ██╗ ███████║██╔████╔██║█████╗    ██║  ██║╚██╗ ██╔╝█████╗  ██████╔╝'), Colors.green))
        WConio2.gotoxy(82, 23)
        print(color(('██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝    ██║  ██║ ╚████╔╝ ██╔══╝  ██╔══██╗'), Colors.green))
        WConio2.gotoxy(82, 24)
        print(color(('╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗  ╚█████╔╝  ╚██╔╝  ███████╗██║  ██║'), Colors.green))
        WConio2.gotoxy(82, 25)
        print(color((' ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝'), Colors.green))
    
        printWithSpecialCharacters("SCORE:", 92, 30)
        printWithSpecialCharacters(pontuacao, 122, 30)


        printWithSpecialCharacters("Press ESC", 94, 40)

        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()

            if key == 27 or key == 7:
                menu()


def getPlayerName():
    init_colorit()
    os.system('cls')
    cursor.hide()
    user_name = ''
    while True:
        WConio2.gotoxy(78, 20)
        print(color(("██╗   ██╗ ██████╗███████╗██████╗   ███╗  ██╗ █████╗ ███╗   ███╗███████╗██╗"), Colors.green))
        WConio2.gotoxy(78, 21)
        print(color(("██║   ██║██╔════╝██╔════╝██╔══██╗  ████╗ ██║██╔══██╗████╗ ████║██╔════╝╚═╝"), Colors.green))
        WConio2.gotoxy(78, 22)
        print(color(("██║   ██║╚█████╗ █████╗  ██████╔╝  ██╔██╗██║███████║██╔████╔██║█████╗"), Colors.green))
        WConio2.gotoxy(78, 23)
        print(color(("██║   ██║ ╚═══██╗██╔══╝  ██╔══██╗  ██║╚████║██╔══██║██║╚██╔╝██║██╔══╝"), Colors.green))
        WConio2.gotoxy(78, 24)
        print(color(("╚██████╔╝██████╔╝███████╗██║  ██║  ██║ ╚███║██║  ██║██║ ╚═╝ ██║███████╗██"), Colors.green))
        WConio2.gotoxy(78, 25)
        print(color((" ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝"), Colors.green))


        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()

            if key == 27 or key == 7:
                menu()
            
            if key == 13:
                return user_name
            
            user_name += symbol
            
            printWithSpecialCharacters(user_name, 82, 32)


def iniciarJogo():
    player_name = getPlayerName()
    player = Player(player_name)

    init_colorit()
    os.system('cls')
    cursor.hide()
    
    
    enemy1 = Enemy(10 + CONST_X, 7)
    enemy2 = Enemy(30 + CONST_X, 7)
    enemy3 = Enemy(50 + CONST_X, 7)
    enemy4 = Enemy(70 + CONST_X, 7)
    enemy5 = Enemy(90 + CONST_X, 7)
    enemy6 = Enemy(110 + CONST_X, 7)
    enemy7 = Enemy(130 + CONST_X, 7)

    enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]


    while True:

        printTela()

        enemy1.iniciarJogo(enemies, player)
        enemy2.iniciarJogo(enemies, player)
        enemy3.iniciarJogo(enemies, player)
        enemy4.iniciarJogo(enemies, player)
        enemy5.iniciarJogo(enemies, player)
        enemy6.iniciarJogo(enemies, player)
        enemy7.iniciarJogo(enemies, player)


        conferirNumeroInimigos(enemies)


        player.shoot(enemies)

        player.printPlayer()
        player.printVidas()

        player.controll()

        if player.is_alive == False:
            gameOver(str(player.pontuacao))

menu()
