import WConio2

while True:
    if WConio2.kbhit():
        (key, symbol) = WConio2.getch()

        print(key, symbol)