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

        opt = input("Alegeți o opțiune: ")

        match opt:
            case "1":
                graf = citire_tastatura()
            case "2":
                numeFis = input("Introduceți numele fișierului cu graful: ")
                graf = citFisGrafOrientat(numeFis)
            case "3":
                if graf is not None:
                    afiseazaGraf(graf)
                else:
                    print("Graful nu a fost încă citit.")
            case "4":
                print("Opțiunea de scriere a fișierului nu este implementată.")
            case "5":
                if graf is not None:
                    s = input("Introduceți nodul sursă: ").strip()
                    t = input("Introduceți nodul țintă: ").strip()

                    drumuri = []
                    gasesteDrumuri(graf, s, t, [], drumuri)

                    print(f"Drumurile între {s} și {t} sunt:")
                    for drum in drumuri:
                        print(drum)
                else:
                    print("Graful nu a fost încă citit.")
            case "0":
                break
            case _:
                print("Opțiune invalidă. Vă rugăm să alegeți o opțiune validă.")

if __name__ == "__main__":
    main()