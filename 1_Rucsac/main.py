from functii import *


while True:
    print("1. Citire tastatura")
    print("2. Citire fisier")
    print("3. Afisare date")
    print("4. Scriere date")
    print("5. Rezolvare")
    opt = int(input("Alege: "))
    match(opt):
        case 1:
            n, volum, obiecte = citire_tastatura()
        case 2:
            n, volum, obiecte = citire_fisier()
        case 3:
            afisare_date(n, volum, obiecte)
        case 4:
            scriere_fisier(n, volum, obiecte)
        case _:
            print("Opțiune invalidă")
