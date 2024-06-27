from functii import *
def main():
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scrierea in fisier")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match(opt):
            case 1:
                n, concurente, matrice = citire_tastatura()
            case 2:
                n, concurente, matrice = citire_fisier()
            case 3:
                afisare_date(n, matrice)
            case 4:
                scriere_fisier(n, matrice)

main()