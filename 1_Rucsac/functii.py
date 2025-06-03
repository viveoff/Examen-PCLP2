def citire_tastatura():
    obiecte = []
    vol_max = int(input("Vol max: "))
    n = int(input("n = "))
    for i in range(n):
        nume = input(f"Nume obiect {i+1}: ")
        volum = int(input(f"Volum obiect {i+1}: "))
        pret = int(input(f"Pret obiect {i+1}: "))
        obiecte.append([nume, volum, pret])
    return n, vol_max, obiecte

def citire_fisier():
    fisier = "intput.txt"
    with open(fisier, "r") as file:
        linii = file.readlines()

    set = int(input("Alege setul: "))
    obiecte = []

    match(set):
        case 1:
            volum = int(linii[0])
            n = int(linii[1])

            for linie in linii[2 : 2 + n]:
                nume, vol_str, pret_str = linie.strip().split()
                vol_obj = int(vol_str)
                pret = int(pret_str)
                obiecte.append([nume, vol_obj, pret])

        case 2:
            volum = int(linii[5])
            n = int(linii[6])

            for linie in linii[7: 7 + n]:
                nume, vol_str, pret_str = linie.strip().split()
                vol_obj = int(vol_str)
                pret = int(pret_str)
                obiecte.append([nume, vol_obj, pret])

        case 3:
            volum = int(linii[10])
            n = int(linii[11])

            for linie in linii[12: 12 + n]:
                nume, vol_str, pret_str = linie.strip().split()
                vol_obj = int(vol_str)
                pret = int(pret_str)
                obiecte.append([nume, vol_obj, pret])

        case 4:
            volum = int(linii[15])
            n = int(linii[16])

            for linie in linii[17: 17 + n]:
                nume, vol_str, pret_str = linie.strip().split()
                vol_obj = int(vol_str)
                pret = int(pret_str)
                obiecte.append([nume, vol_obj, pret])

        case _:
            print("Optiunea invalida")

    return n, volum, obiecte


def afisare_date(n, volum, obiecte):
    print(f"{volum}")
    print(f"{n}")

    for i in range(n):
        nume, volum, pret = obiecte[i]
        print(f"{nume} {volum} {pret}")

def scriere_fisier(volum,n,obiecte):
    with open("out.txt", "w") as file:
        file.write(f"{volum}\n{n}\n")
        for obiect in obiecte:
            nume, volum, pret = obiect
            file.write(f"{nume} {volum} {pret}\n")

def info_autor():
    print("TARYTSA ADRIAN\nGRUPA 3114A")