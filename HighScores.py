import json

# with open ('highscores.json', 'r') as file:
#     highscores = json.load(file)

# highscores.sort(key=lambda x: x["pontuacao"])

# print(highscores)

# nova_pontuacao = {
#     "name": "Ronaldo",
#     "pontuacao": 1950
# }

# for highscore in highscores:
#     if nova_pontuacao["pontuacao"] > highscore["pontuacao"]:
#         highscores.remove(highscore)
        
#         highscores.append(nova_pontuacao)
#         break

# print(highscores)

class Highscores:
    def __init__(self):
        self.readHighscores()

    def readHighscores(self):
        with open ('highscores.json', 'r') as file:
            highscores = json.load(file)

        highscores.sort(key=lambda x: x["pontuacao"], reverse=True)

        self.first = highscores[0]
        self.second = highscores[1]
        self.third = highscores[2]
        self.forth = highscores[3]
        self.fifth = highscores[4]

    