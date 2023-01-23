from colorit import *
import WConio2

from .limiteTela import LimiteTela

character = "█"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
gray = color(character, (180,180,180))
dark_gray = color(character, (125, 125, 125))
light_gray = color(character, (225,225,225))


class Player:
    def __init__(self, player_x, player_y):
        self.pontuacao = 0
        self.x = player_x
        self.y = player_y
    
    def printPlayer(self):
        WConio2.gotoxy(self.x, self.y)
        print(' ' * 7 + light_gray + ' ' * 7)

        WConio2.gotoxy(self.x, self.y + 1)
        print(' ' * 6 + light_gray * 3 + ' ' * 6)
        
        WConio2.gotoxy(self.x, self.y + 2)
        print(' ' * 5 + light_gray * 2 + blue + light_gray * 2 + ' ' * 5)
        
        WConio2.gotoxy(self.x, self.y + 3)
        print(' ' * 4 + light_gray * 2 + blue * 3 + light_gray * 2 + ' ' * 4)
        
        WConio2.gotoxy(self.x, self.y + 4)
        print(' ' * 2 + gray + light_gray * 3 + gray * 3 + light_gray * 3 + gray + ' ' * 2)
        
        WConio2.gotoxy(self.x, self.y + 5)
        print(' '+ gray + light_gray * 4 + dark_gray + red + dark_gray + light_gray * 4 + gray + ' ') 
        
        WConio2.gotoxy(self.x, self.y + 6)
        print(' ' + gray + light_gray * 2 + ' ' * 2 + yellow + red + yellow + ' ' * 2 + light_gray * 2 + gray + ' ') 
        
        WConio2.gotoxy(self.x, self.y + 7)
        print(' ' + dark_gray + gray + ' ' * 4 + yellow + ' ' * 4 + gray + dark_gray + ' ') 

    def shoot(self, enemys):  
        for i in range(51):               
            if LimiteTela.limiteTelaY(self.y - i - 1) == False:
                pass
            else:
                shoot_x = self.x + 7
                shoot_y = self.y - i - 1
                WConio2.gotoxy(shoot_x, shoot_y) 
                print(red)
                WConio2.gotoxy(self.x + 7, self.y - i + 2) 
                print(' ')

            self.conferirTiro(shoot_x, shoot_y, enemys)


    def conferirTiro(self, shoot_x, shoot_y, enemys):
        for enemy in enemys:
            if (enemy.x < shoot_x and shoot_x < enemy.x + 12):
                if (shoot_y == enemy.y):
                    if (enemy.is_alive):
                        self.pontuacao += 50
                    enemy.is_alive = False
        return False
   

    def controll(self):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
    
            if symbol == 'a' or symbol == 'A':
                if LimiteTela.limitePlayerX(self.x - 1) == False:
                    pass
                else:
                    self.x-=1
    
            if symbol == 'd' or symbol == 'D':
                if LimiteTela.limitePlayerX(self.x + 1) == False:
                    pass
                else:
                    self.x+=1
            



