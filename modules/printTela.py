import WConio2

def printTela(pontuacao):
    WConio2.gotoxy(0, 0)
    print("#" * 101)
    print(f" Pontuacao: {pontuacao}")
    for i in range(51):
        WConio2.gotoxy(0, i)
        print("#")
        WConio2.gotoxy(101, i)
        print("#")


    WConio2.gotoxy(0, 50)
    print("#" * 101)
