def citire_fisier():
    set = int(input("Set (1 - 4): "))
    with open("file.txt", "r") as f:
        linii = f.readlines()
        drumuri = []
        match set:
            case 1:
                n = int(linii[0])
                start, stop = map(int, linii[1].split())
                matrice = [[0] * (n+1) for _ in range(n+1)]
                for i, linie in enumerate(linii[2:6]):
                    drumuri_input = linie.split()
                    for d in drumuri_input:
                        if int(d) != 0:
                            j = int(d) - 1
                            matrice[i][j] = 1
                            matrice[j][i] = 1
    return n, start, stop, matrice, drumuri

def afisare(n, start, stop, matrice):
    for i in range(n):
        print(*matrice[i])

def scriere_fisier(n, start, stop, drumuri):
    with open("out.txt", "w") as f:
        for drum in drumuri:
            print(" ".join(map(str, drum))+ "\n")