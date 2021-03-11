print("Ile to 2+2*2?")

lifes = 3

while lifes >= 0:

    answer = int(input("Wynik tego działania to: "))

    if answer != 6:
        lifes -= 1
        print("Błąd! Pozostałe życia:", lifes)
        if lifes == 0:
            lifes = 3
            print ("""Przegrałeś! Spróbuj jeszcze raz!

Ile to 2+2*2?""")
    else:
        print("To jest poprawna odpowiedź! Gratulacje!")
        break
        
    
        
                
