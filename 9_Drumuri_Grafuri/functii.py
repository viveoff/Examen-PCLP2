
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
    graf = {}
    while True:
        linie = input("Introdu nod (de ex: A:B,C): ")
        if linie == "":
            break
        nod, urm = linie.split(":")
        nod = nod.strip()
        urmatori = []
        for urmator in urm.split(','):
            urmator = urmator.strip()
            if urmator:
                urmatori.append(urmator)
        includeNod(nod, urmatori, graf)
    return graf

def gasesteDrumuri(graf, s, t, cale_curenta, drumuri):
    cale_curenta.append(s)
    if s == t:
        drumuri.append(list(cale_curenta))
    else:
        for vecin in graf.get(s, []):
            if vecin not in cale_curenta:  # evită ciclurile
                gasesteDrumuri(graf, vecin, t, cale_curenta, drumuri)
    cale_curenta.pop()

def afiseazaGraf(graf):
    print("Graful citit este:")
    for nod, lst_urm in graf.items():
        print(f"{nod}: {', '.join(lst_urm)}")


