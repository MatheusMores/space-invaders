import WConio2

def printTela():
    WConio2.gotoxy(0, 0)
    print("#" * 101)
    for i in range(51):
        WConio2.gotoxy(0, i)
        print("#")
        WConio2.gotoxy(101, i)
        print("#")


    WConio2.gotoxy(0, 50)
    print("#" * 101)

printTela()