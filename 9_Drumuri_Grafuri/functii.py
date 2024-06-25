def includeNod(nod, lista_vecini, graf):
    if nod in graf:
        graf[nod] += lista_vecini
    else:
        graf[nod] = lista_vecini

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
def citre_fisier():
    graf = dict()
    with open("file.txt", 'r') as f:
        for linie in f:
            nod_crt, urm = linie.strip().split(':')
            nod_crt = nod_crt.strip()
            lst_urm = [t.strip() for t in urm.split(',') if t != '']
            includeNod(nod_crt, lst_urm, graf)
    return graf



def afisare(graf):
    for nod in graf:
        print(f"{nod}: {','.join(graf[nod])}")

# Example usage
if __name__ == "__main__":


    # Reading graph from the keyboard
    graf_din_tastatura = citire_tastatura()
    print("Graph read from keyboard:")
    afisare(graf_din_tastatura)
