from colorit import *
import WConio2


class Menu:
    def __init__(self):
        self.x = 14
        self.y = 5
        self.opcao = 0


    def printMenu(self):
        x = self.x
        y = self.y

        # Space
        WConio2.gotoxy(x, y)
        print(color((' ' * 65 + "//////////    ////////////,    .////////        ///////////    ///////////////"), Colors.green))
        WConio2.gotoxy(x, y + 1)
        print(color((' ' * 63 + ".(((((((((/ //.,(((((((((((. //  *((((((((      // ,(((((((((,  /,,(((((((((((("), Colors.green))
        WConio2.gotoxy(x, y + 2)
        print(color((' ' * 62 + "(((((((((((((( / (((((((((((((/   (((((((((*    . (((((((((((((/ / (((((((((((("), Colors.green))
        WConio2.gotoxy(x, y + 3)
        print(color((' ' * 63 + "((((( / ((((( /,.(((((  .(((((   ((((,*((((    / (((((   *(((( / (((((/"), Colors.green))
        WConio2.gotoxy(x, y + 4)
        print(color((' ' * 64 + "((((( /         (((((   (((((   ((((  ((((    / (((((        ./ ((((("), Colors.green))
        WConio2.gotoxy(x, y + 5)
        print(color((' ' * 64 + ",(((((.,,,, /// .((((.. (((((  .((((  ((((     *((((.        / ((((((((("), Colors.green))
        WConio2.gotoxy(x, y + 6)
        print(color((' ' * 67 + ".(((((((((( / (((((((((((   (((((  ((((/    ((((( /      *.,(((("), Colors.green))
        WConio2.gotoxy(x, y + 7)
        print(color((' ' * 74 + "((((.**.((((((((     ((((((((((((  . ((((/  *(((( / ((((/ //"), Colors.green))
        WConio2.gotoxy(x, y + 8)
        print(color((' ' * 67 + "(((((  .((((   ((((.        ((((*   ((((    ((((   (((( / ((((("), Colors.green))
        WConio2.gotoxy(x, y + 9)
        print(color((' ' * 69 + "(((((((((     ((((        ((((    ((((     (((((((/     (((((((((("), Colors.green))

        # Invaders
        WConio2.gotoxy(x, y + 11)
        print(color((' ' * 43 + "//////   *///*  //////   ////*   ,/////    ////////*     ,///////,./*   .///////**,..   ///////////    ,/////////////"), Colors.green))
        WConio2.gotoxy(x, y + 12)
        print(color((' ' * 40 + "/((((/ / /(((/ / ((((((  *(((( *// ((((((    ((((((((..     ((((((((((((   / (((((((((((( / (((((((((((( /// *((((((((((("), Colors.green))
        WConio2.gotoxy(x, y + 13)
        print(color((' ' * 42 + "((((( ** (((((  (((((( , ((((( / ,(((((    ((((((((( /    ((((   (((((    ((((((       / (((((/  /(((( /  ((((   ,(((("), Colors.green))
        WConio2.gotoxy(x, y + 14)
        print(color((' ' * 44 + "((((( / *((((( (((((( / ((((( / ((((( /  ((((/((((/     ((((   (((((  / ((((( *//   / (((((., (((((   (((((   (((("), Colors.green))
        WConio2.gotoxy(x, y + 15)
        print(color((' ' * 44 + "((((( / *((((( (((((( / ((((( / ((((( /  ((((/((((/     ((((   (((((  / ((((( *//   / (((((., (((((   (((((   (((("), Colors.green))
        WConio2.gotoxy(x, y + 16)
        print(color((' ' * 46 + "((((* / (((((((((((( /, ((((. ((((( /  ((((, (((( /   ((((   (((((   ((((((((((  , /((((   (((*    ((((,"), Colors.green))
        WConio2.gotoxy(x, y + 17)
        print(color((' ' * 47 + "*(((( / ,((((((((((( // (((((.((((,*  /(((./,(((( ,  (((*,,/((((  , (((((        *((((((((((. //   ((((((((*"), Colors.green))
        WConio2.gotoxy(x, y + 18)
        print(color((' ' * 49 + "((((( / ((((( ((((( //, ((((((((( . *(((((((((( *  (((,  (((((   /((((/.//   ,,(((( / (((( / ,,,.   (((("), Colors.green))
        WConio2.gotoxy(x, y + 19)
        print(color((' ' * 51 + "((((.   ((((  .(((     ((((((((   .(((,   ((((   (((((((((     ((((((((((   ((((   (((.   (((((((((/"), Colors.green))


        # New Game
        WConio2.gotoxy(x + 84, y + 26)
        print(color(('█▄  █ █▀▀ █   █    █▀▀█ █▀▀█ █▀▄▀█ █▀▀'), Colors.green))
        WConio2.gotoxy(x + 84, y + 27)
        print(color(('█ █ █ █▀▀ █▄█▄█    █ ▄▄ █▄▄█ █ ▀ █ █▀▀'), Colors.green))
        WConio2.gotoxy(x + 84, y + 28)
        print(color(('█  ▀█ ▀▀▀  ▀ ▀     █▄▄█ ▀  ▀ ▀   ▀ ▀▀▀'), Colors.green))
                        
        # HighScore
        WConio2.gotoxy(x + 81, y + 33)
        print(color(('█  █  ▀  █▀▀▀ █  █ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀'), Colors.green))
        WConio2.gotoxy(x + 81, y + 34)
        print(color(('█▀▀█ ▀█▀ █ ▀█ █▀▀█ ▀▀█ █   █  █ █▄▄▀ █▀▀ ▀▀█'), Colors.green))
        WConio2.gotoxy(x + 81, y + 35)
        print(color(('█  █ ▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀ ▀▀ ▀▀▀ ▀▀▀'), Colors.green))
                        
        # Quit
        WConio2.gotoxy(x + 95, y + 40)
        print(color(('█▀▀█ █  █  ▀  ▀▀█▀▀'), Colors.green))
        WConio2.gotoxy(x + 95, y + 41)
        print(color(('█  █ █  █ ▀█▀   █'), Colors.green))
        WConio2.gotoxy(x + 95, y + 42)
        print(color(('▀▀▀█  ▀▀▀ ▀▀▀   ▀'), Colors.green))

    def selectOpcao(self):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()

            if key == 80:
                self.opcao += 1

            elif key == 72:
                self.opcao -= 1
            
            if self.opcao == 3:
                self.opcao = 0
            
            elif self.opcao == -1:
                self.opcao = 2

            if key == 13 and self.opcao == 0:
                return 0

            if key == 13 and self.opcao == 1:
                return 1

        if self.opcao == 0:
            self.selectNewGame()
        
        elif self.opcao == 1:
            self.selectHighScores()
        
        elif self.opcao == 2:
            self.selectQuit()

    def selectNewGame(self):
        x = self.x
        y = self.y

        whiteSquare = color(('▀'), Colors.white)
        whiteRectangle = color(('█'), Colors.white)

        WConio2.gotoxy(x + 78, y + 31)
        print(' ' * 49)
        for i in range(6):
            WConio2.gotoxy(x + 78, y + 31 + i)
            print(' ')

            WConio2.gotoxy(x + 127, y + 31 + i)
            print(' ')
        
        WConio2.gotoxy(x + 78, y + 37)
        print(' ' * 50)

        WConio2.gotoxy(x + 92, y + 38)
        print(' ' * 25)
 
        for i in range(6):
            WConio2.gotoxy(x + 92, y + 38 + i)
            print(' ')

            WConio2.gotoxy(x + 116, y + 38 + i)
            print(' ')
        
        WConio2.gotoxy(x + 92, y + 44)
        print(' ' * 25)


        WConio2.gotoxy(x + 81, y + 24)
        print(whiteSquare * 44)
        for i in range(6):
            WConio2.gotoxy(x + 81, y + 24 + i)
            print(whiteRectangle)

            WConio2.gotoxy(x + 125, y + 24 + i)
            print(whiteRectangle)
        
        WConio2.gotoxy(x + 81, y + 30)
        print(whiteSquare * 45)
    
    def selectHighScores(self):
        x = self.x
        y = self.y

        whiteSquare = color(('▀'), Colors.white)
        whiteRectangle = color(('█'), Colors.white)
        
        WConio2.gotoxy(x + 81, y + 24)
        print(' ' * 44)
 
        for i in range(6):
            WConio2.gotoxy(x + 81, y + 24 + i)
            print(' ')

            WConio2.gotoxy(x + 125, y + 24 + i)
            print(' ')
        
        WConio2.gotoxy(x + 81, y + 30)
        print(' ' * 45)

        WConio2.gotoxy(x + 92, y + 38)
        print(' ' * 25)
 
        for i in range(6):
            WConio2.gotoxy(x + 92, y + 38 + i)
            print(' ')

            WConio2.gotoxy(x + 116, y + 38 + i)
            print(' ')
        
        WConio2.gotoxy(x + 92, y + 44)
        print(' ' * 25)

        WConio2.gotoxy(x + 78, y + 31)
        print(whiteSquare * 49)
        for i in range(6):
            WConio2.gotoxy(x + 78, y + 31 + i)
            print(whiteRectangle)

            WConio2.gotoxy(x + 127, y + 31 + i)
            print(whiteRectangle)
        
        WConio2.gotoxy(x + 78, y + 37)
        print(whiteSquare * 50)
    
    def selectQuit(self):
        x = self.x
        y = self.y
        whiteSquare = color(('▀'), Colors.white)
        whiteRectangle = color(('█'), Colors.white)

        WConio2.gotoxy(x + 81, y + 24)
        print(' ' * 44)
 
        for i in range(6):
            WConio2.gotoxy(x + 81, y + 24 + i)
            print(' ')

            WConio2.gotoxy(x + 125, y + 24 + i)
            print(' ')
        
        WConio2.gotoxy(x + 81, y + 30)
        print(' ' * 45)
        
        WConio2.gotoxy(x + 78, y + 31)
        print(' ' * 49)
 
        for i in range(6):
            WConio2.gotoxy(x + 78, y + 31 + i)
            print(' ')

            WConio2.gotoxy(x + 127, y + 31 + i)
            print(' ')
        
        WConio2.gotoxy(x + 78, y + 37)
        print(' ' * 50)

        # Printar Quadrado
        WConio2.gotoxy(x + 92, y + 38)
        print(whiteSquare * 25)
 
        for i in range(6):
            WConio2.gotoxy(x + 92, y + 38 + i)
            print(whiteRectangle)

            WConio2.gotoxy(x + 116, y + 38 + i)
            print(whiteRectangle)
        
        WConio2.gotoxy(x + 92, y + 44)
        print(whiteSquare * 25)