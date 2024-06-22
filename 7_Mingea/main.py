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
                citire_tastatura()
            case 2:
                citire_fisier()
            case 3:
                afisare_date()
            case 4:
                scriere_fisier()
            case 5:
                rezolvare()
                if nr_solutie == 0:
                    print("Nu exista solutii.")
                else:
                    print("S-a terminat cautarea. Total solutii gasite:", nr_solutie)

if __name__ == "__main__":
    main()
