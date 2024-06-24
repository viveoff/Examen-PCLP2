from functii import *

def main():
    spectacole = []
    n = 0

    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scriere date")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n, spectacole = citire_tastatura()
            case 2:
                filename = input("Nume fisier: ")
                n, spectacole = citire_fisier(filename)
            case 3:
                afisare(n, spectacole)
            case 4:
                scriere_fisier(spectacole)
            case 5:
                rezolvare(spectacole)
            case 6:
                break
            case _:
                print("Optiune invalida")


if __name__ == "__main__":
    main()
