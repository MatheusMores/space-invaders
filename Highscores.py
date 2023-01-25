import json
import os
from colorit import *

from Characters import printWithSpecialCharacters

class Highscores:
    def __init__(self):
        self.readHighscores()

    def readHighscores(self):
        with open ('highscores.json', 'r') as file:
            highscores = json.load(file)

        highscores.sort(key=lambda x: x["pontuacao"], reverse=True)

        self.highscores = highscores

    def addNewHighScore(self, nova_pontuacao):
        self.highscores.sort(key=lambda x: x["pontuacao"], reverse=True)
        for highscore in self.highscores:
            if nova_pontuacao["pontuacao"] > highscore["pontuacao"]:
                self.highscores.remove(highscore)
                
                self.highscores.append(nova_pontuacao)
                self.highscores.sort(key=lambda x: x["pontuacao"], reverse=True)
                self.saveNewHighscores()

                break
    
    def saveNewHighscores(self):
        with open("highscores.json", "w") as outfile:
            json.dump(self.highscores, outfile)

    def printHighScore(self):
        init_colorit()
        os.system('cls')
        printWithSpecialCharacters('1-', 10, 10)
        printWithSpecialCharacters(f'{self.highscores[0]["name"]}:{self.highscores[0]["pontuacao"]}', 25, 10)


highs = Highscores() 
highs.addNewHighScore({
    "name": "mores",
    "pontuacao": 8900
})
highs.printHighScore()
# highs.addNewHighScore({
#     "name": "Leo",
#     "pontuacao": 5500
# })  
