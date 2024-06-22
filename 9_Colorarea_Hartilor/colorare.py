def citire_tastatura_graf_neorientat():
    graf = {}
    n = int(input("Introduceți numărul de noduri: "))
    for _ in range(n):
        linie = input(f"Introduceți nodul și vecinii săi separați prin virgulă (de exemplu, 'A: B,C'): ")
        nod_crt, urm = linie.strip().split(':')
        nod_crt = nod_crt.strip()
        lst_urm = [t.strip() for t in urm.split(',') if t != '']
        includeNod(nod_crt, lst_urm, graf)
        for x in lst_urm:
            includeNod(x, [nod_crt], graf)
    return graf


def citire_fisier_graf_neorientat():
    graf = {}
    file = open("file.txt", "r")
    linie  = file.readlines()
    for l in linie:
        nod_crt, urm = linie.strip().split(':')
        nod_crt = nod_crt.strip()
        lst_urm = [t.strip() for t in urm.split(',') if t != '']
        includeNod(nod_crt, lst_urm, graf)
        for x in lst_urm:
            includeNod(x, [nod_crt], graf)
    return graf


def includeNod(nod_crt, vecini, graf):
    if nod_crt not in graf:
        graf[nod_crt] = []
    for vecin in vecini:
        if vecin not in graf[nod_crt]:
            graf[nod_crt].append(vecin)

def afisare_graf(graf):
    if not graf:
        print("Graful este gol.")
    else:
        print("Graful citit:")
        for nod, vecini in graf.items():
            print(f"{nod}: {' '.join(vecini)}")

def scriere_fisier(graf):
    with open("out.txt", "w") as f:
        for nod, adiacente in graf.items():
            f.write(f"{nod}: {', '.join(adiacente)}\n")
    print("Scriere fisier cu succes! ")
def main():
    graf = {}  # Inițializează graf ca un dicționar gol aici pentru a fi accesibil în toate opțiunile
    while True:
        print("\nMeniu:")
        print("1. Citire date de la tastatură")
        print("2. Citire fisier")
        print("3. Afisare graf")
        print("4. Scriere fisier")

        optiune = input("Selectați o opțiune: ")

        match optiune:
            case "C":
                graf = citire_tastatura_graf_neorientat()
            case "F":
                graf = citire_fisier_graf_neorientat()  # Corectare: atribuie graful citit din fișier lui "graf"
            case "A":
                afisare_graf(graf)
            case "S":
                scriere_fisier(graf)
            case _:
                print("Opțiune invalidă! Vă rugăm să selectați o opțiune validă.")

if __name__ == "__main__":
    main()
