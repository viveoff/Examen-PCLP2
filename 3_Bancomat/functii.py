bancnote_disponibile = []
suma_ceruta = 0

def citire_tastatura():
    bancnote = []
    nr_bancnote = int(input("Nr de bancnote: "))
    valori_bancnote = []
    for _ in range(nr_bancnote):
        valoare_bancnota = int(input("Valoare bancnota: "))
        valori_bancnote.append(valoare_bancnota)
    for valoare in valori_bancnote:
        cantitate_bancnote = int(input(f"Introdu cantitatea pentru bancnota de {valoare}: "))
        bancnote.append((valoare, cantitate_bancnote))
    return bancnote


def citire_fisier(fis):
    global bancnote_disponibile
    try:
        n = int(fis.readline().strip())
        if n <= 0:
            raise ValueError("Numărul de bancnote trebuie să fie pozitiv și nenul.")
        bancnote_disponibile = []
        for _ in range(n):
            linie = fis.readline().strip()
            if linie:
                valoare_bancnota, cantitate_bancnota = map(int, linie.split())
                bancnote_disponibile.append((valoare_bancnota, cantitate_bancnota))
            else:
                raise ValueError("Linie goală detectată în timpul citirii bancnotelor.")
        print("Citire din fișier cu succes")
        return n, bancnote_disponibile

    except ValueError as ve:
        print("Eroare la citirea din fișier:", ve)
        return None, None

    except Exception as e:
        print("Eroare necunoscută la citirea din fișier:", e)
        return None, None


def afisare_date(bancnote_disponibile):
    if not bancnote_disponibile:
        print("Lista de bancnote este goală.")
        return

    print("Bancnote disponibile:")
    for valoare, cantitate in bancnote_disponibile:
        print(f"Valoare: {valoare} | Cantitate: {cantitate}")

def scrier_fisier(n, bancnote_disponibile):
    with open("out.txt", "w") as f:
        f.write(f"{n}\n")
        for valoare, cantitate in bancnote_disponibile:
            f.write(f"{valoare} {cantitate}\n")
        print("Scrierer fisier!")




def bancomat(suma, bancnote, afis=True):
    bancnote.sort(reverse=True)
    if afis:
        print("Suma=", suma, "Bancnote disponibile:", bancnote)
    rez = []
    while suma > 0:
        if len(bancnote) == 0:
            break
        if suma >= bancnote[0][0]:
            nr_bancnote = suma // bancnote[0][0]
            suma = suma % bancnote[0][0]
            rez.append([bancnote[0][0], nr_bancnote])
        bancnote.pop(0)
    else:
        return rez
    return []

def livrare(pachet):
    if len(pachet) == 0:
        print("Nu dispunem de bancnotele necesare")
    else:
        for val, nr in pachet:
            print(nr, "x", val, "lei", end=" ")
            print()

