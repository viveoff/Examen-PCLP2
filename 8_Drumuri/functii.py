def citire_tastatura():
    global n, start, stop, sosele
    n = int(input("Introduceti numarul de orase: "))
    start, stop = map(int, input("Introduceti orasul de start si orasul de destinatie separate prin spatiu: ").split())

    # Initializare matrice sosele
    sosele = []
    for i in range(n):
        drumuri_input = input(f"Drumuri pentru orasul {i + 1}: ").split()
        drumuri = [0] * n
        for drum in drumuri_input:
            if int(drum) != 0:
                drumuri[int(drum) - 1] = 1
        sosele.append(drumuri)

    return n, start, stop, sosele

# functii.py

def citire_fisier(file_name):
    global n, start, stop, sosele
    with open(file_name, 'r') as f:
        n = int(f.readline().strip())
        start, stop = map(int, f.readline().strip().split())

        sosele = []
        for i in range(n):
            drumuri_input = f.readline().strip().split()
            drumuri = [0] * n
            for drum in drumuri_input:
                if int(drum) != 0:
                    drumuri[int(drum) - 1] = 1
            sosele.append(drumuri)

    return n, start, stop, sosele

def afisare_matrice(sosele):
    for linie in sosele:
        print(' '.join(map(str, linie)))
