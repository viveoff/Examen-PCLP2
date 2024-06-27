def citire_tastatura():
    n = int(input("n = "))
    cote = n * [None]
    cale = n * [None]
    for i in range(n):
        cote[i] = [int(x) for x in input("Cote: ").split()]
        cale[i] = [0] * n
    x0 = int(input("x = "))
    y0 = int(input("y = "))
    return n, cote, x0, y0

def citire_fisier():
    with open("file.txt", "r") as f:
        linii = f.readlines()
        n = int(linii[0])
        cote = n * [None]
        cale = n * [None]
        for i, linie in enumerate(linii[1:4]):
            cote[i] = linie.split()
            cale[i] = [0] * n
        x0 = int(linii[5])
        y0 = int(linii[6])
    return n, cote, x0, y0
def afisare(n, cote, x0 ,y0):
    for i in range(n):
        print(*cote[i])

def scriere_fisier(n, cote, x0, y0):
    with open("out.txt", "w") as f:
        for i in range(n):
            f.write(" ".join(map(str, cote[i])) + "\n")
