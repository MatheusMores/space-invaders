import json

class Highscores:
    def __init__(self):
        self.readHighscores()

    def readHighscores(self):
        with open ('highscores.json', 'r') as file:
            highscores = json.load(file)

        highscores.sort(key=lambda x: x["pontuacao"])

        self.highscores = highscores

    def addNewHighScore(self, nova_pontuacao):
        for highscore in self.highscores:
            if nova_pontuacao["pontuacao"] > highscore["pontuacao"]:
                self.highscores.remove(highscore)
                
                self.highscores.append(nova_pontuacao)
                self.highscores.sort(key=lambda x: x["pontuacao"])
                self.saveNewHighscores()

                break
    
    def saveNewHighscores(self):
        with open("highscores.json", "w") as outfile:
            json.dump(self.highscores, outfile)


highs = Highscores() 
# highs.addNewHighScore({
#     "name": "Leo",
#     "pontuacao": 5500
# })  
