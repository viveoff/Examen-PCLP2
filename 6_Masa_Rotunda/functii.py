def citire_tastatura():
    n = int(input("n = "))
    concurente = []
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        concurenti_input = input(f"Concurente a lui {i+1}: ").split()
        for c in concurenti_input:
            if int(c) != 0:
                j = int(c) - 1
                matrice[i][j] = 1
                matrice[j][i] = 1
    concurente.append(concurenti_input)
    return n, concurente, matrice



def citire_fisier():
    set_number = int(input("Set (1 - 4): "))
    with open("file.txt", "r") as f:
        concurente = []
        linii = f.readlines()
        match set_number:
            case 1:
                n = int(linii[0].strip())
                matrice = [[0] * n for _ in range(n)]
                for i, linie in enumerate(linii[1:1+n]):
                    concurenti_input = list(map(int, linie.split()))
                    for c in concurenti_input:
                        if c != 0:
                            j = c - 1
                            matrice[i][j] = 1
                            matrice[j][i] = 1
                concurente.append(concurenti_input)
            case 2:
                n = int(linii[5].strip())
                matrice = [[0] * n for _ in range(n)]
                for i, linie in enumerate(linii[6:6 + n]):
                    concurenti_input = list(map(int, linie.split()))
                    for c in concurenti_input:
                        if c != 0:
                            j = c - 1
                            matrice[i][j] = 1
                            matrice[j][i] = 1
                concurente.append(concurenti_input)
    return n, concurente, matrice

def afisare_date(n, matrice):
    for i in range(n):
        print(*matrice[i])

def scriere_fisier(n, matrice):
    with open("out.txt", "w") as f:
        f.write(f"{n}\n")
        for input_line in matrice:
            f.write(" ".join(map(str, input_line)) + "\n")
