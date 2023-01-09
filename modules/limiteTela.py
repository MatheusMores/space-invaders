
class LimiteTela:
    def __init__(self):
        self.x = 233
        self.y = 300
    
    @classmethod
    def limitePlayerX(self, player_x):
        if player_x + 23 >= 233:
            return False

        if player_x <= 0:
            return False
        
    @classmethod
    def limitePlayerY(self, player_y):
        
        if player_y >= 45:
            return False
        
        if player_y <= 0:
            return False