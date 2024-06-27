from functii import *

def main():
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scrierea in fisier")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n, cote, x0, y0 = citire_tastatura()
            case 2:
                n, cote, x0, y0 = citire_fisier()
            case 3:
                afisare(n, cote, x0, y0)
            case 4:
                scriere_fisier(n, cote, x0, y0)

if __name__ == "__main__":
    main()
