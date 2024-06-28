def includeNod(nod, lista_vecini, graf):
    if nod in lista_vecini:
        graf[nod] += lista_vecini
    else:
        graf[nod] = lista_vecini
def citire_tastatura():
    graf = dict()

    while True:
        linie = input("Nod: ")
        if linie == '':
            break

        nod, urm = linie.split(':')
        nod = nod.strip()
        lista_vecini = [vec.strip() for vec in urm.split(',') if vec != '']

        includeNod(nod, lista_vecini, graf)

    return graf

def afisare(graf):
    print(graf)

