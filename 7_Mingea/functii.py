def citire_tastatura():
    n = int(input("n = "))
    cote = n * [None]
    cale = n * [None]
    for i in range(n):
        cote[i] = [int(x) for x in input("Cote (0,0,0): ").split()]
        cale[i] = [0] * n
    x0 = int(input("x0 = "))
    y0 = int(input("y0 = "))
    return n, cote, x0, y0

def citire_fisier():
    with open("file.txt", "r") as f:
        linii = f.readlines()
        set = int(input("Set (1 - 4): "))
        match set:
            case 1:
                n = int(linii[0])
                cote = n * [None]
                cale = n * [None]
                for i, linie in enumerate(linii[1:4]):
                    cote[i] = linie.split()
                x0 = int(linii[4])
                y0 = int(linii[5])

    return n, cote, x0, y0

def afisare_date(n, cote, x0, y0):
    print(f"Coordonate initiale: {x0}, {y0}")
    for i in range(n):
        print(*cote[i])

def scrier_fisier(cote, x0, y0):
    with open("out.txt", "w") as f:
        f.write(f"{x0} {y0}\n")
        for linie in cote:
            f.write(' '.join(map(str, linie)) + "\n")


