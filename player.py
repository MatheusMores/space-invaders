from colorit import *
import WConio2
from characters import printWithSpecialCharacters

from limiteTela import CONST_X, LimiteTela, limitesTela
from highscore import Highscores
 
character = "█"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
gray = color(character, (180,180,180))
dark_gray = color(character, (125, 125, 125))
light_gray = color(character, (225,225,225))


class Player:
    def __init__(self, name):
        self.name = name
        self.tiros_tomados = []
        self.vidas = 3
        self.is_alive = True
        self.pontuacao = 0
        self.x = int(limitesTela['x'] / 2) - 4 + CONST_X
        self.y = limitesTela['y'] - 10
    
    def printPlayer(self):
        WConio2.gotoxy(self.x, self.y)
        print(' ' * 8 + light_gray + ' ' * 8)

        WConio2.gotoxy(self.x, self.y + 1)
        print(' ' * 7 + light_gray * 3 + ' ' * 7)
        
        WConio2.gotoxy(self.x, self.y + 2)
        print(' ' * 6 + light_gray * 2 + blue + light_gray * 2 + ' ' * 6)
        
        WConio2.gotoxy(self.x, self.y + 3)
        print(' ' * 5 + light_gray * 2 + blue * 3 + light_gray * 2 + ' ' * 5)
        
        WConio2.gotoxy(self.x, self.y + 4)
        print(' ' * 3 + gray + light_gray * 3 + gray * 3 + light_gray * 3 + gray + ' ' * 3)
        
        WConio2.gotoxy(self.x, self.y + 5)
        print(' ' * 2+ gray + light_gray * 4 + dark_gray + red + dark_gray + light_gray * 4 + gray + ' ' * 2) 
        
        WConio2.gotoxy(self.x, self.y + 6)
        print(' ' * 2+ gray + light_gray * 2 + ' ' * 2 + yellow + red + yellow + ' ' * 2 + light_gray * 2 + gray + ' ' * 2) 
        
        WConio2.gotoxy(self.x, self.y + 7)
        print(' ' * 2+ dark_gray + gray + ' ' * 4 + yellow + ' ' * 4 + gray + dark_gray + ' ' * 2) 

    def printVidas(self):
        for vida in range(int(self.vidas)):
            WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 2)
            print('  ' + red * 2 + '  ' + red * 2 + '  ')
            WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 3)
            print(red * 10)
            WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 4)
            print('  ' + red * 6 + '  ')
            WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 5)
            print('  ' * 2 + red * 2 + '  ' * 2)

    def perderVida(self, shoot_id):
        if (shoot_id not in self.tiros_tomados):
            self.tiros_tomados.append(shoot_id)

            for vida in range(self.vidas):
                WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 2)
                print('  ' * 7)
                WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 3)
                print('  ' * 7)
                WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 4)
                print('  ' * 7)
                WConio2.gotoxy((limitesTela['x'] - 11 - vida * 12) + CONST_X, limitesTela['y'] + 5)
                print('  ' * 7)
            self.vidas -= 1
        
        if self.vidas == 0:
            Highscores.addNewHighScore({
                "name": self.name,
                "pontuacao": self.pontuacao
            })

            self.is_alive = False
    
    def printPontuacao(self):
        printWithSpecialCharacters("SCORE: ", CONST_X, limitesTela['y'] + 2)
        
        for i in range(len(str(self.pontuacao))):
            printWithSpecialCharacters("<", CONST_X + 30 + 4 * i, limitesTela['y'] + 2)
        
        printWithSpecialCharacters(str(self.pontuacao), CONST_X + 30, limitesTela['y'] + 2)
            

    def shoot(self, enemies):  
        for i in range(limitesTela['y']):               
            if LimiteTela.limiteTelaY(self.y - i - 1) == False:
                pass
            else:
                shoot_x = self.x + 7
                shoot_y = self.y - i - 1
                for j in range(3):
                    WConio2.gotoxy(shoot_x, shoot_y - j) 
                    print(red)
                WConio2.gotoxy(self.x + 7, self.y - i + 2) 
                print(' ')

            self.conferirTiro(shoot_x, shoot_y, enemies)

    def conferirTiro(self, shoot_x, shoot_y, enemies):
        for enemy in enemies:
            if (enemy.x < shoot_x and shoot_x < enemy.x + 12):
                if (shoot_y == enemy.y):
                    if (enemy.is_alive):
                        self.pontuacao += 150
                    enemy.is_alive = False
                    
        return False
   

    def controll(self):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
    
            if symbol == 'a' or symbol == 'A':
                if LimiteTela.limitePlayerX(self.x - 2) == False:
                    pass
                else:
                    self.x-=2
    
            if symbol == 'd' or symbol == 'D':
                if LimiteTela.limitePlayerX(self.x + 2) == False:
                    pass
                else:
                    self.x+=2
    



