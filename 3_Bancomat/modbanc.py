def citire_fis():
    with open('banc.txt', 'r') as f:
        linii = f.readlines()
        n = 0
        bancnote = []
        sett = int(input('Introdu setul cu care vrei sa lucrezi: '))
        match sett:
            case 1:
                for line in linii[0:4]:
                    parti = line.strip().split()
                    nominal = int(parti[0])
                    cantit = int(parti[1])
                    n += 1
                    bancnote.append((nominal, cantit))
            case 2:
                for line in linii[4:8]:
                    parti = line.strip().split()
                    nominal = int(parti[0])
                    cantit = int(parti[1])
                    n += 1
                    bancnote.append((nominal, cantit))
            case 3:
                for line in linii[8:11]:
                    parti = line.strip().split()
                    nominal = int(parti[0])
                    cantit = int(parti[1])
                    n += 1
                    bancnote.append((nominal, cantit))
        return bancnote, n

def citire_tast():
    bancnote = []
    n = int(input('Introdu numarul de bancnote disponibile in bancomat: '))
    for i in range(n):
        nominal = int(input('Introdu nominalul bancnotei: '))
        cantit = int(input(f'Cate bancnote de {nominal} sunt: '))
        bancnote.append((nominal, cantit))
    return bancnote, n

def afisare(bancnote, n):
    print(f'Numarul de bancnote in bancomat este: {n}')
    for banc in bancnote:
        print(f'Bancnote de {banc[0]} sunt {banc[1]}')