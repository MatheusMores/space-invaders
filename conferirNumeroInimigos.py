import random

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