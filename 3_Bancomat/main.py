from functii import *

def main():

    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scriere date")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n, bancnote = citire_tastatura()
            case 2:
                fisier = input("Nume fisier: ")
                bancnote = citire_fisier(fisier)
            case 3:
                afisare(bancnote)
            case 4:
                scriere_fisier(bancnote)
            case 5:
                suma_ceruta = int(input("Suma ceruta: "))
                pachet = bancomat(suma_ceruta, bancnote)
                livrare(pachet)


if __name__ == "__main__":
    main()