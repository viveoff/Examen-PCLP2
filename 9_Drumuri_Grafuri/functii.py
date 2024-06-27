def includeNod(nod, lista_vecini, graf):
    if nod in graf:
        graf[nod] += lista_vecini
    else:
        graf[nod] = lista_vecini
def citire_tastatura():
    graf = dict()
    while True:
        linie = input("Nod: ").strip()
        if linie == '':
            break

        nod, vecini = linie.split(":")
        nod = nod.strip()
        lista_vecini = [vecin.strip() for vecin in vecini.split(",") if vecin.strip()]
        includeNod(nod, lista_vecini, graf)
    return graf

def citire_fisier():
    graf = dict()
    set = int(input("Set (1 - 4): "))
    with open("file.txt", "r") as f:
        linii = f.readlines()
        for linie in linii[0:3]:
            nod, vecini = linie.split(":")
            nod = nod.strip()
            lista_vecini = [v.strip() for v in vecini.split(",") if v.strip()]
            includeNod(nod, lista_vecini, graf)
    return graf
def afisare(graf):
    print(graf)


