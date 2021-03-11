#guess the number

number = 14

while(True):
    playerNumber = int(input("Podaj Twoją liczbę: "))
    if (playerNumber > number):
        print("To za dużo")
    elif (playerNumber < number):
        print("To za mało")
    else:
        print("Bingo!")
        break
