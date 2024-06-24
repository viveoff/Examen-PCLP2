from functii import *
def main():

    while True:
        print("1. Citire de la tastatura")
        print("2. Citire din fisier")
        print("3. Afisare matrice podurilor")
        print("4. Scriere fisier")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n, ins_start, poduri = citire_tastatura()
            case 2:
                fisier = input("Nume fisier: ")
                n, ins_start, poduri = citire_fisier(fisier)
            case 3:
                afisare(n, ins_start, poduri)
            case 4:
                scrier_fisier(n, ins_start, poduri)
            case 5:
                Plimbare(ins_crt, k)



if __name__ == "__main__":
    main()