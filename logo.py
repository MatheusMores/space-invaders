from colorit import *
import WConio2


def printLogo(x, y):
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
                    
