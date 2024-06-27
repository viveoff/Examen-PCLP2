from funcii import *

def main():
    n = s = d = 0
    matrice = []
    drumuri = []
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare matrice")
        print("4. Scriere fisier")
        print("5. Rezolvare")

        opt = int(input("Alege: "))

        match opt:
            case 1:
                n,s, d, matrice, drumuri = citire_tastatura()
            case 2:
                n, s, d, matrice, drumuri = citire_fisier()
            case 3:
                afisare(n, s, d, matrice)
            case 4:
                scriere_fisier(n, s, d, drumuri)


if __name__ == "__main__":
    main()
