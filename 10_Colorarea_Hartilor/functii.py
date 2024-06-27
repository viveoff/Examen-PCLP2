def includeNod(nod_crt, nod_urm, graf):
    if nod_crt in graf:
        graf[nod_crt] += nod_urm
    else:
        graf[nod_crt] = nod_urm

def citire_tastatura():
    graf = dict()

    while True:
        linie = input("Nod: ").strip()
        if linie == '':
            break

        nod_crt, nod_urm_str = linie.split(":")
        nod_crt = nod_crt.strip()
        nod_urm = [vec.strip() for vec in nod_urm_str.split(",") if vec.strip()]

        includeNod(nod_crt, nod_urm, graf)

        for vec in nod_urm:
            includeNod(vec, [nod_crt], graf)

    return graf

def citire_fisier():
    graf = dict()
    set = int(input("Set (1 - 4): "))
    with open("file.txt", "r") as file:
        linii = file.readlines()
        match set:
            case 1:
                for linie in linii[0:6]:
                    nod_crt, nod_urm_str = linie.split(":")
                    nod_crt = nod_crt.strip()

                nod_urm = [vec.strip() for vec in nod_urm_str.split(",") if vec.strip()]

                includeNod(nod_crt, nod_urm, graf)

                for vec in nod_urm:
                    includeNod(vec, [nod_crt], graf)
    return graf

def afisare(graf):
    print(graf)