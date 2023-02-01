import json
from colorit import *
import WConio2

from characters import printWithSpecialCharacters

class Highscores:

    def readHighscores(self):
        with open ('highscores.json', 'r') as file:
            highscores = json.load(file)

        highscores.sort(key=lambda x: x["pontuacao"], reverse=True)

        self.highscores = highscores

    @classmethod
    def addNewHighScore(self, nova_pontuacao):
        self.readHighscores(self)
        self.highscores.sort(key=lambda x: x["pontuacao"])
        for highscore in self.highscores:
            if nova_pontuacao["pontuacao"] > highscore["pontuacao"]:
                self.highscores.remove(highscore)
                
                self.highscores.append(nova_pontuacao)
                self.highscores.sort(key=lambda x: x["pontuacao"], reverse=True)
                self.saveNewHighscores(self)

                break
    
    def saveNewHighscores(self):
        with open("highscores.json", "w") as outfile:
            json.dump(self.highscores, outfile)

    @classmethod
    def printHighScore(self):
        self.readHighscores(self)

        WConio2.gotoxy(80, 15)
        print(color(('██╗  ██╗██╗ ██████╗ ██╗  ██╗ ██████╗ █████╗  █████╗ ██████╗ ███████╗ ██████╗'), Colors.green))
        WConio2.gotoxy(80, 16)
        print(color(('██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝'), Colors.green))
        WConio2.gotoxy(80, 17)
        print(color(('███████║██║██║  ██╗ ███████║╚█████╗ ██║  ╚═╝██║  ██║██████╔╝█████╗  ╚█████╗'), Colors.green))
        WConio2.gotoxy(80, 18)
        print(color(('██╔══██║██║██║  ╚██╗██╔══██║ ╚═══██╗██║  ██╗██║  ██║██╔══██╗██╔══╝   ╚═══██╗'), Colors.green))
        WConio2.gotoxy(80, 19)
        print(color(('██║  ██║██║╚██████╔╝██║  ██║██████╔╝╚█████╔╝╚█████╔╝██║  ██║███████╗██████╔╝'), Colors.green))
        WConio2.gotoxy(80, 20)
        print(color(('╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝'), Colors.green))
        
        i = 0
        for score in self.highscores:
            printWithSpecialCharacters(f'{i + 1}-', 83, 25 + 6 * i)
            printWithSpecialCharacters(f'{score["name"]}:{score["pontuacao"]}', 93, 25 + 6 * i)
            i += 1


