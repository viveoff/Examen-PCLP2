def citire_tastatura():
    n = int(input("n = "))
    concurente = []
    for i in range(n):
        concurenti_input = input(f"Concurente a lui {i+1}: ").split()
        concurenti = [0] * n
        for c in concurenti_input:
            concurenti[int(c) - 1] = 1
        concurente.append(concurenti)
    return n, concurente

def citire_fisier(fisier):
    set = int(input("Set (1 - 4): "))
    with open(fisier, "r") as f:
        concurente = []
        linii = f.readlines()
        match set:
            case 1:
                n = int(linii[0].strip())
                for linie in linii[1:n+1]:
                    concurenti_input = list(map(int, linie.strip().split()))
                    concurenti = [0] * n
                    for c in concurenti_input:
                        concurenti[c - 1] = 1
                    concurente.append(concurenti)
            case 2:
                n = int(linii[5].strip())
                for linie in linii[6:n + 6]:
                    concurenti_input = list(map(int, linie.strip().split()))
                    concurenti = [0] * n
                    for c in concurenti_input:
                        concurenti[c - 1] = 1
                    concurente.append(concurenti)
    return n, concurente

def afisare(n, concurente):
    for i in range(n):
        print(*concurente[i])