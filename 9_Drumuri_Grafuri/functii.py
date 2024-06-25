def includeNod(nod, lst_urm, graf):
    if nod in graf:
        graf[nod] += lst_urm
    else:
        graf[nod] = lst_urm

def citFisGrafOrientat(numeFis):
    graf = dict()
    with open(numeFis, 'r') as f:
        for linie in f:
            nod_crt, urm = linie.strip().split(':')
            nod_crt = nod_crt.strip()
            lst_urm = [t.strip() for t in urm.split(',') if t != '']
            includeNod(nod_crt, lst_urm, graf)
    return graf

def citire_tastatura():
    graf = dict()
    print("Enter graph data (format: node: neighbor1, neighbor2, ...). Enter 'done' when finished:")
    while True:
        linie = input().strip()
        if linie.lower() == 'done':
            break
        nod_crt, urm = linie.split(':')
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
