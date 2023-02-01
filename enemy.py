import random
from colorit import *
import uuid
import WConio2
from limiteTela import LimiteTela, limitesTela

character = "█"

green = color(character, Colors.green)

class Enemy:
    def __init__(self, enemy_x, enemy_y):
        self.is_alive = True
        self.enemy_id = uuid.uuid4()
        self.x = enemy_x
        self.y = enemy_y

    def iniciarJogo(self, enemies, player):
        self.mover(enemies)
        self.printEnemy()
        self.shoot(player)


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
    
    def shoot(self, player):
        if self.is_alive == True:
            aleatorio = random.randint(0, 5)
            if aleatorio == 2:
                shoot_id = uuid.uuid4()
                for i in range(limitesTela['y'] - self.y - 10):               
                    shoot_x = self.x + 6
                    shoot_y = self.y + i + 10
                    for j in range(5):
                        WConio2.gotoxy(shoot_x, shoot_y + j) 
                        print(green)
                    WConio2.gotoxy(self.x + 6, self.y + i + 9) 
                    print(' ')
                    WConio2.gotoxy(self.x + 6, limitesTela['y'] - 1) 
                    print('#')
                    for j in range(5):
                        WConio2.gotoxy(self.x + 6, limitesTela['y'] + j) 
                        print(' ')

                    self.conferirTiro(shoot_x, shoot_y, shoot_id, player)

    def mover(self, enemies):
        if self.is_alive == True:
            aleatorio = random.randint(0, 2)
            enemies_position = [enemy.x for enemy in enemies]

            if aleatorio == 0:
                if LimiteTela.limiteEnemyX(self.x + 7) == False:
                    pass
                elif self.x + 15 in enemies_position:
                    pass
                else:
                    for i in range(100):
                        if i == 6:
                            self.x += 1

            if aleatorio == 1:
                if LimiteTela.limiteEnemyX(self.x - 7) == False:
                    pass
                elif self.x - 15 in enemies_position:
                    pass
                else:
                    for i in range(100):
                        if i == 6:
                            self.x -= 1

    def conferirTiro(self, shoot_x, shoot_y, shoot_id, player):
        if (player.x < shoot_x and shoot_x < player.x + 12):
            if (shoot_y == player.y):
                player.perderVida(shoot_id)
                    
        return False
   
          
def conferirNumeroInimigos(enemies):
    contador_inimigos = 0

    for enemy in enemies:
        if enemy.is_alive == True:
            contador_inimigos+= 1
    
    if contador_inimigos == 3:
        for enemy in enemies:
            aleatorio = random.randint(0, 1)
            if aleatorio == 0:
                enemy.is_alive = True


