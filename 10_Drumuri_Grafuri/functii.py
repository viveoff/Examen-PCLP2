def citire_tastatura():
    n = int(input("Introduceți numărul de orașe: "))
    start = int(input("Introduceți orașul de start: "))
    destinatie = int(input("Introduceți orașul de destinație: "))
    sosele = [[] for _ in range(n + 1)]
    print("Introduceți drumurile între orașe (format: oraș1 oraș2 oraș3 ... orașN, terminați cu o linie goală):")
    while True:
        linie = input()
        if linie == "":
            break
        orase = list(map(int, linie.split()))
        for oras in orase[1:]:
            sosele[orase[0]].append(oras)
    return (n, start, destinatie, sosele)

def includeNod(nod, lst_urm, graf):
    if nod in graf:
        graf[nod] += lst_urm
    else:
        graf[nod] = lst_urm


def cauta_drumuri(graf, nod_crt, stop, cale=[]):
    cale = cale + [nod_crt]
    if nod_crt == stop:
        return [cale]
    if nod_crt not in graf:
        return []
    toateDrumurile = []
    for nod in graf[nod_crt]:
        if nod not in cale:
            drumuri = cauta_drumuri(graf, nod, stop, cale)
            for drum in drumuri:
                toateDrumurile.append(drum)
    return toateDrumurile


def cauta_cale(graf, oras_crt, stop, cale=[]):
    cale = cale + [oras_crt]
    if oras_crt == stop:
        return cale
    if oras_crt not in graf:
        return None
    for oras_urm in graf[oras_crt]:
        if oras_urm not in cale:
            drum = cauta_cale(graf, oras_urm, stop, cale)
            if drum:
                return drum
    return None


def citeste(numeFisier):
    with open(numeFisier, 'r') as f:
        n, start, destinatie = map(int, f.readline().split())
        sosele = [[] for _ in range(n + 1)]
        for linie in f:
            orase = list(map(int, linie.split()[:-1]))
            for oras in orase:
                sosele[orase[0]].append(oras)
    return (n, start, destinatie, sosele)


def afisare_date(n, start, destinatie, sosele):
    print(f"Număr de orașe: {n}")
    print(f"Start: {start}")
    print(f"Destinație: {destinatie}")
    print("Șoselele:")
    for i in range(1, len(sosele)):
        print(f"{i}: {', '.join(map(str, sosele[i]))}")

def rezolva_problema(n, start, destinatie, sosele):
    # Transformăm lista de șosele într-un graf pentru funcțiile cauta_drumuri și cauta_cale
    graf = {i: [] for i in range(1, n + 1)}
    for i in range(1, len(sosele)):
        for oras in sosele[i]:
            graf[i].append(oras)

    drumuri = cauta_drumuri(graf, start, destinatie)
    cale = cauta_cale(graf, start, destinatie)

    if drumuri:
        print("Toate drumurile de la start la destinație:")
        for drum in drumuri:
            print(" -> ".join(map(str, drum)))
    else:
        print("Nu există drumuri de la start la destinație.")

    if cale:
        print("O cale de la start la destinație:")
        print(" -> ".join(map(str, cale)))
    else:
        print("Nu există o cale de la start la destinație.")
