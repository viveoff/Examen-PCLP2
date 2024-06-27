def includeNod(nod_crt, nod_urm, graf):
    if nod_crt in graf:
        graf[nod_crt] += nod_urm
    else:
        graf[nod_crt] = nod_urm


# Graf neorientat

def citire_tastatura():
    graf = dict()

    print("Nod: ")
    while True:
        linie = input().strip()
        if linie == '':
            break

        nod_crt, nod_urm_str = linie.split(":")
        nod_crt = nod_crt.strip()
        nod_urm = [vec.strip() for vec in nod_urm_str.split(",") if vec.strip()]

        includeNod(nod_crt, nod_urm, graf)

        for vec in nod_urm:
            includeNod(vecin, [nod_crt], graf)

    return graf

def afisare(graf):
    print(graf)