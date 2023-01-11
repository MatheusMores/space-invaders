
class LimiteTela:
    def __init__(self):
        self.x = 101
    
    
    @classmethod
    def limitePlayerX(self, player_x):
        if player_x + 15 >= 101:
            return False

        if player_x <= 0:
            return False