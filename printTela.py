import WConio2

from limiteTela import limitesTela


def printTela(pontuacao):
    WConio2.gotoxy(0, 0)
    print("#" * limitesTela['x'])
    print(f" Pontuacao: {pontuacao}")
    for i in range(limitesTela['y']):
        WConio2.gotoxy(0, i)
        print("#")
        WConio2.gotoxy(limitesTela['x'], i)
        print("#")


    WConio2.gotoxy(0, limitesTela['y'] - 1)
    print("#" * limitesTela['x'])
