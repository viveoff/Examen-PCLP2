from modbanc import *

def main():
    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        opt = int(input("Introdu optiunea: "))
        match opt:
            case 1:
                bancnote, n = citire_tast()
            case 2:
                bancnote, n = citire_fis()
            case 3:
                afisare(bancnote, n)

if __name__ == '__main__':
    main()

