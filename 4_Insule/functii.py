def citire_tastatura(n, ins_start, pod):
    vector = []
    n = int(input("Nr poduri: "))
    ins_start = int(input("Insula start: "))
    for i in range(n):
        poduri = input(f"Pod {i+1}: ").split()
        pod = [int(num) for num in poduri]
        vector.append(pod)
    return n, ins_start, vector


def afisare(vector):
    for pod in vector:
        print(" ".join(map(str, pod)))


def citire_fisier(fisier):
    vector = []
    try:
        n = int(fisier.readline())
        inst_start = int(fisier.readline().strip())
        for i in range(n):
            poduri = fisier.readline().strip().split()
            pod = [int(num) for num in poduri]
            vector.append(pod)
        return n, inst_start, vector
    except ValueError:  # End of file or invalid data
        return None, None, None


def scriere_fisier(n, ins_start, vector):
    with open("out.txt", "w") as f:
        f.write(f"{n}\n")
        f.write(f"{ins_start}\n")
        for pod in vector:
            f.write(" ".join(map(str, pod)) + "\n")
    print("Scriere fisier cu succes!")

