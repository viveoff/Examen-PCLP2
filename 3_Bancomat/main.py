from functii import *

def main():
    n = 0
    global bancnote_disponibile, suma_ceruta
    fis = None

    while True:
        print("1. Citire date de la tastatura")
        print("2. Citire date din fisier")
        print("3. Afisare date citite")
        print("4. Rezolvare problema")
        print("5. Scriere fisier")
        print("6. Exit")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                bancnote_disponibile = citire_tastatura()
            case 2:
                if fis is None:
                    fis = open("file.txt","r")
                n, bancnote_disponibile = citire_fisier(fis)
                if n is None:
                    print("-")
                    fis.close()
                    fis = None
            case 3:
                afisare_date(bancnote_disponibile)
            case 4:
                suma_ceruta = int(input("Introdu suma dorita: "))
                pachet = bancomat(suma_ceruta, bancnote_disponibile)
                livrare(pachet)
            case 5:
                scrier_fisier(n, bancnote_disponibile)
            case 6:
                break

if __name__ == "__main__":
    main()