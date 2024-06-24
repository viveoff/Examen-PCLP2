from functii import cauta_drumuri, cauta_cale, citire_tastatura, citeste, afisare_date, rezolva_problema

def main():
    n, start, destinatie, sosele = 0, 0, 0, []
    while True:
        print("\nMeniu:")
        print("1. Citire date de la tastatură")
        print("2. Citire date din fișier")
        print("3. Afișare date citite")
        print("4. Rezolvare")

        opt = input("Alegeți o opțiune: ")

        match opt:
            case "1":
                n, start, destinatie, sosele = citire_tastatura()
            case "2":
                numeFisier = "file.txt"
                n, start, destinatie, sosele = citeste(numeFisier)
                print("Citire din fișier cu succes")
            case "3":
                if n > 0:
                    afisare_date(n, start, destinatie, sosele)
                else:
                    print("Nu există date de afișat. Citiți mai întâi datele.")
            case "4":
                rezolva_problema(n, start, destinatie, sosele)
            case _:
                print("Opțiune invalidă! Vă rugăm să selectați o opțiune validă.")


if __name__ == "__main__":
    main()
