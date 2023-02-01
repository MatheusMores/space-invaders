import WConio2

from limiteTela import CONST_X, limitesTela


def printTela():
    WConio2.gotoxy(0 + CONST_X, 0)
    print("#" * limitesTela['x'])
    for i in range(limitesTela['y']):
        WConio2.gotoxy(0 + CONST_X, i)
        print("#")
        WConio2.gotoxy(limitesTela['x'] + CONST_X, i)
        print("#")


    WConio2.gotoxy(0 + CONST_X, limitesTela['y'] - 1)
    print("#" * limitesTela['x'])
