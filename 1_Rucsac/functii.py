def citire_tastatura():
    obiecte = []
    vol_max = int(input("Vol max: "))
    n = int(input("n = "))
    for i in range(n):
        nume = input(f"Nume obiect {i+1}: ")
        volum = int(input(f"Volum obiect {i+1}: "))
        pret = int(input(f"Pret obiect {i}: "))
        obiecte.append([nume, volum, pret])
    return n, volum, obiecte

def citire_fisier():
    fisier = input("Nume fisier: ")
    with open(fisier, "r") as file:
        linii = file.readlines()
        set = int(input("Alege setul: "))
        obiecte = []
        match(set):
            case 1:
                n = int(linii[1])
                volum = int(linii[0])
                for linie in linii[2:7]:
                    nume, volum, pret = list(map(str, linie.strip().split()))
                    volum, pret = int(volum), int(pret)
                    obiecte.append([nume, volum, pret])
            case 2:
                n = int(linii[8])
                volum = int(linii[7])
                for linie in linii[9:12]:
                    nume, volum, pret = list(map(str, linie.strip().split()))
                    volum, pret = int(volum), int(pret)
                    obiecte.append([nume, volum, pret])
        return n, volum, obiecte


def afisare_date(n, volum, obiecte):
    print(f"{volum}")
    print(f"{n}")
    for i in range(n):
        nume, volum, pret = obiecte[i]
        print(f"{nume} {volum} {pret}")

def scriere_fisier(n, volum, obiecte):
    with open("out.txt", "w") as file:
        file.write(f"{n}\n{volum}\n")
        for obiect in obiecte:
            nume, volum, pret = obiect
            file.write(f"{nume} {volum} {pret}\n")

