from functii import *
def main():
    graf = None

    while True:
        print("\nMeniu:")
        print("1. Citire date de la tastatură")
        print("2. Citire date din fișier")
        print("3. Afișare date citite")
        print("4. Scriere fisier (opțiunea nu este implementată)")
        print("5. Rezolvare")
        print("0. Ieșire")

        opt = int(input("Alegeți o opțiune: "))

        match opt:
            case 1:
                graf = citire_tastatura()
            case 2:
                graf = citre_fisier()
            case 3:
                afisare(graf)


if __name__ == "__main__":
    main()