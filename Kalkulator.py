choose = input("""Podaj symbol działania:
+ - dodawanie
- - odejmowanie
* - mnożenie
/ - dzielenie
** - potęgowanie
% - reszta z dzielenia
Twój wybór: """)
  
 
a = int(input("Podaj pierwszą liczbę działania: "))
b = int(input("Podaj drugą liczbę działania: "))

if(choose == '+'):
    print(a + b)
elif(choose == '-'):
    print(a - b)
elif(choose == '*'):
    print(a * b)
elif(choose == '/'):
    if(b == 0):
        print("Spaliłeś procesor")
    else:
        print(a / b)
elif(choose == '**'):
    print(a ** b)
elif(choose == '%'):
    if(b == 0):
        print("Spaliłeś procesor")
    else:
        print(a % b)
else:
    print("Dokonałeś niepoprawnego wyboru")
    
    
    
    
