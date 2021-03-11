number = int(input("Podaj liczbę: "))

if(number < 0):
    absoluteNumber = number * -1
    print("Wartość bezwzględna Twojej liczby to: " + str(absoluteNumber))

else:
    print("Wartość bezwzględna Twojej liczby to: " + str(number))
    
