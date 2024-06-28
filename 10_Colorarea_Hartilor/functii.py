def includeNod(nod_crt, lista_vecini, graf):
    if nod_crt in graf:
        graf[nod_crt] += lista_vecini
    else:
        graf[nod_crt] = lista_vecini

def citire_tastatura():
    graf = dict()
    while True:
        linie = input("Nod:").strip()
        if linie == '':
            break

        nod, urm = linie.split(':')
        nod = nod.strip()
        lista_vecini = [vec.strip() for vec in urm.split(',') if vec != '']
        includeNod(nod, lista_vecini, graf)
        for x in lista_vecini:
            includeNod(x, [nod], graf)
    return graf
def citire_fisier():
    graf = dict()
    with open("file.txt", "r") as f:
        for linie in f:
            nod_crt, nod_urm = linie.strip().split(':')
            nod_crt = nod_crt.strip()
            lista_vecini = [vec.strip() for vec in nod_urm.split(',') if vec !='']
            includeNod(nod_crt, lista_vecini, graf)
            for x in lista_vecini:
                includeNod(x, [nod_crt], graf)

    return graf

def afisare(graf):
    print(graf)
