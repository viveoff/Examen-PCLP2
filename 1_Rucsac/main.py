from functii import *
global fis

while True:
    print("1. Citire tastatura")
    print("2. Citire fisier")
    print("3. Afisare date")
    print("4. Scriere date")
    print("5. Rezolvare")
    opt = int(input("Alege: "))
    match(opt):
        case 1:
            citire_tastatura()
        case 2:
            if fis is None:
              fis = open("file.txt", "r")
              citire_fisier(fis)
            fis.close()
            fis = None
        case 3:
            afisare_date()
        case 4:
            scriere_fisier()
        case 5:
            rezolvare()
        case _:
            print("Opțiune invalidă")
