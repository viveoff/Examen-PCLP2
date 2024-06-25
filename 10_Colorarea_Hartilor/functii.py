def includeNod(nod_crt, nod_urm, graf):
    if nod_crt in graf:
        graf[nod_crt] += nod_urm
    else:
        graf[nod_crt] = nod_urm


# Graf neorientat
def citire_tastatura():
    graf = dict()
    print("Noduri: ")
    while True:
        linie = input().strip()
        if linie.lower() == '':
            break
        nod_crt, nod_urm = linie.split(":")
        nod_crt = nod_crt.strip()
        lista_vecini = []
        for urm in nod_urm.split(","):
            if urm:
                lista_vecini.append(urm.strip())
        includeNod(nod_crt, lista_vecini, graf)
        for x in lista_vecini:
            includeNod(x, [nod_crt], graf)

    return graf

def afisare(graf):
    print(graf)
