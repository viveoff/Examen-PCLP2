# main.py

from functii import *

def main():
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare matrice")
        print("4. Iesire")

        opt = int(input("Alege: "))

        match opt:
            case 1:
                n, start, stop, sosele = citire_tastatura()
            case 2:
                fisier = input("Introdu numele fisierului: ")
                n, start, stop, sosele = citire_fisier(fisier)
            case 3:
                afisare_matrice(sosele)
            case 4:
                print("Programul s-a incheiat.")
                break
            case _:
                print("Optiune invalida. Alege din nou.")

if __name__ == "__main__":
    main()
