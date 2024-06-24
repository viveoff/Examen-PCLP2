def citire_tastatura():
    spectacole = []
    n = int(input("Nr de spectacole: "))
    for i in range(n):
        nume = input("Denumire spectacol: ")
        start = input("Start HH:MM : ")
        end = input("Sfarsit HH:MM : ")
        ore_start, min_start = map(int, start.strip().split(":"))
        ore_end, min_end = map(int, end.strip().split(":"))
        spectacole.append((nume, ore_start, min_start, ore_end, min_end))
    return n, spectacole


def citire_fisier(filename):
    spectacole = []

    with open(filename, "r") as f:
        linii = f.readlines()

        setul = int(input("Setul (1 - 4): "))

        match setul:
            case 1:
                n = int(linii[0].strip())
                for linie in linii[1:5]:
                    parte = linie.strip().split()
                    nume = parte[0]
                    ore_start, min_start, ore_end, min_end = int(parte[1]), int(parte[2]), int(parte[3]), int(parte[4])
                    spectacole.append((nume, ore_start, min_start, ore_end, min_end))

            case 2:
                n = int(linii[5].strip())
                for linie in linii[6:9]:
                    parte = linie.strip().split()
                    nume = parte[0]
                    ore_start, min_start, ore_end, min_end = int(parte[1]), int(parte[2]), int(parte[3]), int(parte[4])
                    spectacole.append((nume, ore_start, min_start, ore_end, min_end))

            case 3:
                n = int(linii[8].strip())
                for linie in linii[9:12]:
                    parte = linie.strip().split()
                    nume = parte[0]
                    ore_start, min_start, ore_end, min_end = int(parte[1]), int(parte[2]), int(parte[3]), int(parte[4])
                    spectacole.append((nume, ore_start, min_start, ore_end, min_end))

            case 4:
                n = int(linii[12].strip())
                for linie in linii[13:17]:
                    parte = linie.strip().split()
                    nume = parte[0]
                    ore_start, min_start, ore_end, min_end = int(parte[1]), int(parte[2]), int(parte[3]), int(parte[4])
                    spectacole.append((nume, ore_start, min_start, ore_end, min_end))

            case _:
                print("Set invalid!")
                return None, []

    return n, spectacole

def afisare(n, spectacole):
    print("Nr de spectacole: ", n)
    for i in range(n):
        nume, ore_start, min_start, ore_end, min_end = spectacole[i]
        print(f"Spectacolul {nume}: {ore_start:02d}:{min_start:02d} - {ore_end:02d}:{min_end:02d}")


def scriere_fisier(spectacole):
    with open("out.txt", "w") as f:
        for spectacol in spectacole:
            nume, ore_start, min_start, ore_end, min_end = spectacol
            f.write(f"{nume} {ore_start:02d}:{min_start:02d} - {ore_end:02d}:{min_end:02d}\n")


def rezolvare(spectacole):
    # Transformăm spectacolele în minute pentru sortare și selecție
    spectacole_minute = [(nume, ore_start * 60 + min_start, ore_end * 60 + min_end) for
                         nume, ore_start, min_start, ore_end, min_end in spectacole]

    # Sortăm spectacolele după ora de finalizare
    spectacole_minute.sort(key=lambda x: x[2])

    # Lista pentru a ține evidența spectacolelor selectate
    spectacole_selectate = []

    # Ultima oră de finalizare considerată
    ora_ultima_selectata = -1

    for spectacol in spectacole_minute:
        nume, start, end = spectacol
        if start >= ora_ultima_selectata:
            spectacole_selectate.append(spectacol)
            ora_ultima_selectata = end

    # Afișăm spectacolele selectate
    print("Spectacole selectate pentru vizionare:")
    for spectacol in spectacole_selectate:
        nume, start, end = spectacol
        ore_start = start // 60
        min_start = start % 60
        ore_end = end // 60
        min_end = end % 60
        print(f"{nume}: {ore_start:02d}:{min_start:02d} - {ore_end:02d}:{min_end:02d}")

