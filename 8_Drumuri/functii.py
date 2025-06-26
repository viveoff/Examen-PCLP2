def citire_tastatura():
    n = int(input("Nr de orase: "))
    start, stop = map(int, input("Orasele de start si destinatie: ").split())
    matrice = []
    drumuri = []
    for i in range(n):
        drumuri_input = input(f"Drumuri pentru orasul {i+1}: ").split()
        mat = [0] * n
        for d in drumuri_input:
            if int(d) != 0:
                mat[int(d) - 1] = 1
        matrice.append(mat)
        drumuri.append(drumuri_input)
    return n,start, stop, matrice, drumuri


def citire_fisier():
    matrice = []
    drumuri = []
    with open("file.txt", "r") as f:
        set = int(input("Set (1 -4): "))
        linii = f.readlines()
        match set:
            case 1:
                n = int(linii[0])
                start, stop = linii[1].strip().split()
                start, stop = int(start), int(stop)
                for linie in linii[2:6]:
                    drumuri_input = linie.split()
                    mat = [0] * n
                    for d in drumuri_input:
                        if int(d) != 0:
                            mat[int(d) - 1] = 1
                    matrice.append(mat)
                    drumuri.append(drumuri_input)
            case 2:
                n = int(linii[6])
                start, stop = linii[7].strip().split()
                start, stop = int(start), int(stop)
                for linie in linii[8:13]:
                    drumuri_input = linie.split()
                    mat = [0] * n
                    for d in drumuri_input:
                        if int(d) != 0:
                            mat[int(d) - 1] = 1
                    matrice.append(mat)
                    drumuri.append(drumuri_input)
    return n, start, stop, matrice, drumuri


def afisare(n, matrice):
    for i in range(n):
        print(*matrice[i])

def scriere_fisier(n, start, stop, drumuri):
    with open("out.txt", "w") as f:
        f.write(f"{start} {stop}\n")
        f.write(f"{n}\n")
        for drum in drumuri:
            f.write(" ".join(map(str, drum)) + "\n")