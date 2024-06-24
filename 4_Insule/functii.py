def citire_tastatura():
    poduri = []
    n = int(input("n = "))
    ins_start = int(input("Insula de start: "))
    for _ in range(n):
        pod = [int(x) for x in input("Poduri intre insule: ").split()]
        poduri.append(pod)
    return n, ins_start, poduri

def citire_fisier(fisier):
    poduri = []
    with open(fisier,"r") as file:
        linii = file.readlines()
        set = int(input("Set (1 - 4): "))
        match set:
            case 1:
                n = int(linii[0].strip())
                ins_start = int(linii[1])
                for linie in linii[2:7]:
                    pod = list(map(int, linie.strip().split()))
                    poduri.append(pod)
            case 2:
                n = int(linii[7].strip())
                ins_start = int(linii[8].strip())
                for linie in linii[9:12]:
                    pod = list(map(int, linie.strip().split()))
                    poduri.append(pod)
            case 3:
                n = int(linii[0]).strip()
                ins_start = int(linii[1])
                for linie in linii[2:7]:
                    pod = list(map(int, linie.strip().split()))
                    poduri.append(pod)
        return n, ins_start, poduri


def afisare(n, ins_start, poduri):
    print(f"Numar de insule: {n}")
    print("Insula de start: ", ins_start)
    for pod in poduri:
        print(*pod)

def scrier_fisier(n, ins_start, poduri):
    with open("out.txt", "w") as file:
        file.write(f"{n}\n")
        file.write(f"{ins_start}\n")
        for pod in poduri:
            file.write(" ".join(map(str, pod)) + "\n")


