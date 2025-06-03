from functii import *


while True:
    print("1. Citire tastatura")
    print("2. Citire fisier")
    print("3. Afisare date")
    print("4. Scriere date")
    print("5. Rezolvare")
    print("6.Exit")
    opt = int(input("Alege: "))
    match(opt):
        case 1:
            n, volum, obiecte = citire_tastatura()
        case 2:
            n, volum, obiecte = citire_fisier()
        case 3:
            afisare_date(n, volum, obiecte)
        case 4:
            scriere_fisier(volum, n, obiecte)
        case 5:
            info_autor()
        case 6:
            break
        case _:
            print("Opțiune invalidă")