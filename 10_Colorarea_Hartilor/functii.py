def includeNod(nod_crt, urm, graf):
    if nod_crt in graf:
        graf[nod_crt] += urm
    else:
        graf[nod_crt] = urm
def citire_tastatura():
    graf = dict()
    while True:
        linie = input("Nod: ")
        if linie == "":
            break
        nod_crt, nod_urm = linie.split(":")
        nod_crt = nod_crt.strip()
        urmatori = []
        for urmator in nod_urm.split(";"):
            urmator = urmator.strip()
            if urmator:
                urmatori.append(urmator)
        includeNod(nod_crt, urmatori, graf)
    return graf

def citire_fisier():
    graf = {}
    nume_fisier = "file.txt"  # Replace with your file path
    try:
        with open(nume_fisier, "r") as f:
            linii = f.readlines()
            for linie in linii[:6]:  # Adjust as per your file structure
                linie = linie.strip()
                if linie:
                    nod_crt, urm = linie.split(":")
                    nod_crt = nod_crt.strip()
                    urm = [urmator.strip() for urmator in urm.split(",") if urmator.strip()]
                    includeNod(nod_crt, urm, graf)
    except FileNotFoundError:
        print(f"File '{nume_fisier}' not found.")
    return graf

def afisare_date(graf):
    for nod_crt in graf:
        urm = graf[nod_crt]
        for urmator in urm:
            print(f"{nod_crt} {urmator}")

