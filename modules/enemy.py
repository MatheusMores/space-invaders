from colorit import *
import uuid
import WConio2
from .limiteTela import LimiteTela

character = "█"

green = color(character, Colors.green)
eyes = color("■", (0, 0, 0))

class Enemy:
    def __init__(self, enemy_x, enemy_y):
        self.is_alive = True
        self.enemy_id = uuid.uuid4()
        self.x = enemy_x
        self.y = enemy_y
    
    def printEnemy(self):
        if (self.is_alive):
            WConio2.gotoxy(self.x, self.y)
            print(' ' * 3 + green + ' ' * 5 + green + ' ' * 3)
            
            WConio2.gotoxy(self.x, self.y + 1)
            print(' ' * 4 + green + ' ' * 3 + green + ' ' * 4)
            
            WConio2.gotoxy(self.x, self.y + 2)
            print(' ' * 3 + green * 7 + ' ' * 3)
            
            WConio2.gotoxy(self.x, self.y + 3)
            print(' ' * 2 + green * 2 + ' ' + green * 3 + ' ' + green * 2 + ' ' * 2)
            
            WConio2.gotoxy(self.x, self.y + 4)
            print(' ' + green + ' ' + green * 7 + ' ' + green + ' ')
            
            WConio2.gotoxy(self.x, self.y + 5)
            print(' ' + green + ' ' + green + ' ' * 5 + green + ' ' + green + ' ')
            
            WConio2.gotoxy(self.x, self.y + 6)
            print(' ' * 4 + green * 2 + ' ' + green * 2 + ' ' * 4)        
        
        else:
            WConio2.gotoxy(self.x, self.y)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 1)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 2)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 3)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 4)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 5)
            print(' ' * 13)
            
            WConio2.gotoxy(self.x, self.y + 6)
            print(' ' * 13)  

            



