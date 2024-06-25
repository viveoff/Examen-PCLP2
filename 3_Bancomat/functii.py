def citire_tastatura():
    bancnote = []
    n = int(input("n  = "))
    for i in range(n):
        valoare = int(input(f"Valoare pentru bancnota {i+1}: "))
        cantitate = int(input(f"Cantitate bancnote {valoare}: "))
        bancnote.append((valoare, cantitate))
    return n, bancnote

def citire_fisier(fisier):
    bancnote = []
    with open(fisier, "r") as file:
        set = int(input("Set (1 - 4): "))
        linii = file.readlines()
        match(set):
            case 1:
                for linie in linii[0:4]:
                    parte = linie.strip().split()
                    valoare = int(parte[0])
                    cantitate = int(parte[1])
                    bancnote.append((valoare, cantitate))
            case 2:
                for linie in linii[4:8]:
                    parte = linie.strip().split()
                    valoare = int(parte[0])
                    cantitate = int(parte[1])
                    bancnote.append((valoare, cantitate))
        return  bancnote

def afisare(bancnote):
    print(f"Nr de bancnote: {len(bancnote)}")
    for bancnota in bancnote:
        print(f"Valoare: {bancnota[0]} | Cantitate: {bancnota[1]}")

def scriere_fisier(bancnote):
    with open("output.txt", "w") as file:
        file.write(f"{len(bancnote)}\n")
        for valoare, cantitate in bancnote:
            file.write(f"{valoare} {cantitate}\n")
    print("Scriere fisier!")

def bancomat(suma, bancnote, afisare = True):
    bancnote.sort(reverse = True)
    if afisare:
        print(f"Suma: {suma}, Bancnote disponible: {bancnote}")
    rez = []
    while suma > 0:
        if len(bancnote) == 0:
            break
        if suma >= bancnote[0][0]:
            cantitate = suma // bancnote[0][0]
            suma = suma % bancnote[0][0]
            rez.append([bancnote[0][0], cantitate])
        bancnote.pop(0)
    else:
        return rez
    return []

def livrare(pachet):
    if len(pachet) == 0:
        print("Nu dispunem bancnote necesare")
    else:
        for valoare, cantitate in pachet:
            print(f"{cantitate} x {valoare} lei", end = " ")
            print()


