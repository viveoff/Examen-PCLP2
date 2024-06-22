from functii import *
def main():
    n = 0
    ins_start = 0
    vector = []
    fisier = None

    while True:
        print("1. Citire de la tastatura")
        print("2. Citire din fisier")
        print("3. Afisare matrice drumurilor")
        print("4. Scriere fisier")
        print("5. Iesire")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n, ins_start, vector = citire_tastatura(n, ins_start, vector)
            case 2:
                if fisier is None:
                    fisier = open("file.txt", "r")
                n, ins_start, vector = citire_fisier(fisier)
                if n is None:
                    print("Nu mai sunt date de citit din fisier.")
                    fisier.close()
                    fisier = None
            case 3:
                afisare(vector)
            case 4:
                scriere_fisier(n, ins_start, vector)



if __name__ == "__main__":
    main()