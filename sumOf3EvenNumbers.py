#sum of 3 even numbers
i = 0
sumOfNumbers = 0
while i < 3:
    number = int(input("Podaj liczbę parzystą: "))
    
    if(number > 0 and number % 2 == 0):
        sumOfNumbers += number
        i += 1
        
    else:
        print("Podałeś niepoprawną liczbę")
        continue

if (i == 3):
    print("Suma podanych liczb wynosi", sumOfNumbers)
