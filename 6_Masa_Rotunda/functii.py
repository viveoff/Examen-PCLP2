def citire_tastatura():
    n = int(input("n = "))
    concurente = []
    matrice = []
    for i in range(n):
        concurenti_input = input(f"Concurente a lui {i+1}: ").split()
        concurenti = [0] * n
        for c in concurenti_input:
            concurenti[int(c) - 1] = 1
        concurente.append(concurenti)
        matrice.append(concurenti_input)
    return n, concurente, matrice

def citire_fisier(fisier):
    set = int(input("Set (1 - 4): "))
    with open(fisier, "r") as f:
        concurente = []
        matrice = []
        linii = f.readlines()
        match set:
            case 1:
                n = int(linii[0])
                for linie in linii[1:5]:
                    concurenti_input = list(map(int, linie.split()))
                    matrice.append(concurenti_input)
                    concurenti = [0] * n
                    for c in concurenti_input:
                        concurenti[int(c) - 1] = 1
                        concurente.append(concurenti)
            case 2:
                n = int(linii[5])
                for linie in linii[6:8]:
                    concurenti_input = list(map(int, linie.split()))
                    matrice.append(concurenti_input)
                    concurenti = [0] * n
                    for c in concurenti_input:
                        concurenti[int(c) - 1] = 1
                        concurente.append(concurenti)

    return n, concurente, matrice

def afisare(n, concurente):
    for i in range(n):
        print(*concurente[i])

def scriere_fisier(n, matrice):
    with open("out.txt", "w") as f:
        f.write(f"{n}\n")
        for input_line in matrice:
            f.write(" ".join(map(str, input_line)) + "\n")
