from functii import citire_tastatura, afisare, citire_fisier, scriere_fisier, rezolvare

def main():
    while True:
        print("1. Citire date de la tastatura")
        print("2. Citire date din fisier")
        print("3. Afisare date citite")
        print("4. Scriere date")
        print("5. Rezolvare problema")
        print("6. Info autor")
        print("7. Exit")

        opt = int(input("Alege: "))
        match(opt):
            case 1:
                citire_tastatura()
            case 2:
                citire_fisier()
            case 3:
                afisare()
            case 4:
                scriere_fisier()
            case 5:
                rezolvare()
            case 6:
                print("Proiect realizat de Pitu Gabriela-Casandra, gr 3111")
            case 7:
                break
            case _:
                print("Optiune invalida")

if __name__ == "__main__":
    main()
