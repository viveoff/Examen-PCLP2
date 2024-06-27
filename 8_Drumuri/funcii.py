def citire_tastatura():
    n = int(input("n = "))
    s, d = map(int, input("s, d = ").split())
    s -= 1
    d -= 1

    drumuri = []
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        drumuri_input = input(f"Drumuri pt orasul {i+1}: ").split()
        for d in drumuri_input:
            if int(d) != 0:
                j = int(d) - 1
                matrice[i][j] = 1
                matrice[j][i] = 1
        drumuri.append(drumuri_input)
    return n, s, d, matrice, drumuri

def citire_fisier():
    set = int(input("Set (1 - 4): "))
    with open("file.txt", "r") as f:
        linii = f.readlines()
        drumuri = []
        match set:
            case 1:
                n = int(linii[0])
                s, d = map(int, linii[1].split())
                s -= 1
                d -= 1
                matrice = [[0] * n for _ in range(n)]
                for i, linie in enumerate(linii[2:2+n]):
                    drumuri_input = linie.split()
                    for d in drumuri_input:
                        if int(d) != 0:
                            j = int(d) - 1
                            matrice[i][j] = 1
                            matrice[j][i] = 1
                    drumuri.append(drumuri_input)
            case 2:
                n = int(linii[6])
                s, d = map(int, linii[7].split())
                s -= 1
                d -= 1
                matrice = [[0] * n for _ in range(n)]
                for i, linie in enumerate(linii[8:8+n]):
                    drumuri_input = linie.split()
                    for d in drumuri_input:
                        if int(d) != 0:
                            j = int(d) - 1
                            matrice[i][j] = 1
                            matrice[j][i] = 1
    return n, s, d, matrice, drumuri

def afisare(n, s, d, matrice):
    for i in range(n):
        print(*matrice[i])

def scriere_fisier(n, s, d , drumuri):
    with open("out.txt", "w") as f:
        for drum in drumuri:
            f.write(" ".join(map(str, drum)) + "\n")


