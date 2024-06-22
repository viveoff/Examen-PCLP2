vol_max = 0
n = 5
obiecte = []
fis = None

def citire_tastatura():
    global n, vol_max, obiecte
    vol_max = int(input("Introdu volum rucsac: "))
    n = int(input("Introdu nr de obiecte: "))
    obiecte = []
    for i in range(n):
        vol_obiect = int(input(f"Introdu volum obiect {i + 1}: "))
        pret_obiect = int(input(f"Introdu pret obiect {i + 1}: "))
        obiecte.append((vol_obiect, pret_obiect))

def afisare_date():
    print(f"Volum max: {vol_max}")
    print(f"Nr de obiecte: {n}")
    for i in range(n):
        vol_obiect, pret_obiect = obiecte[i]
        print(f"Obiectul {i + 1} are volum {vol_obiect} si pret {pret_obiect}")

def citire_fisier(fis):
    global n, vol_max, obiecte
    try:
        vol_max = int(fis.readline().strip())
        n = int(fis.readline().strip())
        obiecte = []
        for _ in range(n):
            vol_obiect, pret_obiect = map(int, fis.readline().strip().split())
            obiecte.append((vol_obiect, pret_obiect))
        print("Citire din fisier cu succes")
    except Exception as e:
        print("Eroare la citirea din fișier:", e)

def scriere_fisier():
    with open("out.txt", "w") as f:
        f.write(f"{vol_max}\n")
        f.write(f"{n}\n")
        for vol_obiect, pret_obiect in obiecte:
            f.write(f"{vol_obiect} {pret_obiect}\n")
    print("Scriere cu succes")

def rezolvare():
    global vol_max, n, obiecte

    # Sortăm obiectele după preț/volum descrescător
    lista = sorted(obiecte, key=lambda x: x[1] / x[0], reverse=True)

    vt = pt = 0
    x = [0] * n
    i = 0

    while vt < vol_max and i < n:
        if vt + lista[i][0] <= vol_max:  # lista[i][0] este volumul obiectului
            x[i] = 1
            pt += lista[i][1]  # lista[i][1] este prețul obiectului
            vt += lista[i][0]
        else:
            x[i] = (vol_max - vt) / lista[i][0]
            vt = vol_max
            pt += lista[i][1] * x[i]
        i += 1

    print(f"Prețul total al obiectelor din rucsac: {pt:.0f}\nVolumul ocupat = {vt:.2f}")
    print("În rucsac s-au introdus:")
    for i in range(n):
        if x[i] > 0:
            vol_intr = obiecte[i][0] * x[i]
            print(f"Obiectul {i + 1} (Volum: {vol_intr:.2f}, Preț: {obiecte[i][1]})")
