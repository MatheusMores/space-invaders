
class LimiteTela:
    
    @classmethod
    def limitePlayerX(self, player_x):
        if player_x + 15 >= limitesTela['x']:
            return False

        if player_x <= 0:
            return False

    @classmethod
    def limiteEnemyX(self, enemy_x):
        if enemy_x + 15 >= limitesTela['x']:
            return False

        if enemy_x <= 0:
            return False
    
    @classmethod
    def limiteTelaY(self, y):
        if y <= -3:
            return False

limitesTela = {
    'x': 150,
    'y': 60
}