from  functii import *

def main():
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare matrice")
        print("4. Scriere fisier")
        print("5. Rezolvare")

        opt = int(input("Alege: "))

        match opt:
            case 1:
                n, start, stop, matrice, drumuri = citire_tastatura()
            case 2:
                n, start, stop, matrice, drumuri = citire_fisier()
            case 3:
                afisare(n, start, stop, matrice)
            case 4:
                scriere_fisier(n, start, stop, drumuri)


if __name__ == "__main__":
    main()
