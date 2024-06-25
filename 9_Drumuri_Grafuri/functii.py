def includeNod(nod, lista_vecini, graf):
    if nod in graf:
        graf[nod] += lista_vecini
    else:
        graf[nod] = lista_vecini

# Graf orientat
def citire_tastatura():
    graf = dict()
    print("Noduri: ")
    while True:
        linie = input().strip()
        if linie.lower() =='':
            break
        nod, vecini = linie.split(":")
        nod = nod.strip()

        lista_vecini = []
        for vecin in vecini.split(","):
            if vecin:
                lista_vecini.append(vecin.strip())
        includeNod(nod, lista_vecini, graf)
    return graf

def citire_fisier():
    graf = dict()
    set = int(input("Set (1 - 4): "))
    lista_vecini = []

    with open("file.txt", 'r') as f:
        linii = f.readlines()
        match set:
            case 1:
                for linie in linii[0:6]:
                    nod, vecini = linie.split(":")
                    for vecin in vecini.split(","):
                        if vecin.strip():
                            lista_vecini.append(vecin.strip())
                    includeNod(nod.strip(), lista_vecini, graf)
                    lista_vecini = []
            case 2:
                for linie in linii[6:10]:
                    nod, vecini = linie.split(":")
                    for vecin in vecini.split(","):
                        if vecin.strip():
                            lista_vecini.append(vecin.strip())
                    includeNod(nod.strip(), lista_vecini, graf)
                    lista_vecini = []
    return graf

def afisare(graf):
    print(graf)

def scriere_fisier(graf):
    with open("out.txt", 'w') as f:
        for nod, vecini in graf.items():
            linie = f"{nod}:{','.join(vecini)}\n"
            f.write(linie)
