def citire_tastatura():
    graf = {}
    print("Introduceți lista de muchii (nod: succesor1,succesor2,...). Pentru a opri introducerea, lăsați linia goală.")
    while True:
        linie = input().strip()
        if not linie:
            break
        nod, succesori = linie.split(':')
        nod = nod.strip()
        succ_list = [succ.strip() for succ in succesori.split(',') if succ.strip()]
        graf[nod] = succ_list
    return graf


def afisare_matrice_adiacenta(graf):
    noduri = sorted(graf.keys())  # Sortăm nodurile în ordine alfabetică
    nr_noduri = len(noduri)

    # Inițializăm o matrice de adiacență cu 0
    matrice = [[0] * nr_noduri for _ in range(nr_noduri)]

    # Umplem matricea de adiacență
    for i in range(nr_noduri):
        nod_crt = noduri[i]
        if nod_crt in graf:
            for succesor in graf[nod_crt]:
                if succesor in noduri:
                    j = noduri.index(succesor)
                    matrice[i][j] = 1

    # Afișăm matricea de adiacență
    print("Matricea de adiacență:")
    # Afișăm antetul cu nodurile
    print("  ", " ".join(noduri))
    for i in range(nr_noduri):
        print(noduri[i], " ".join(map(str, matrice[i])))

def cauta_drum_cel_mai_scurt(graf, nod_crt, stop, cale=[]):
    cale = cale + [nod_crt]
    if nod_crt == stop:
        return cale
    if nod_crt not in graf:
        return None

    drum_cel_mai_scurt = None
    for nod_urm in graf[nod_crt]:
        if nod_urm not in cale:
            drum = cauta_drum_cel_mai_scurt(graf, nod_urm, stop, cale)
            if drum:
                if not drum_cel_mai_scurt or len(drum) < len(drum_cel_mai_scurt):
                    drum_cel_mai_scurt = drum

    return drum_cel_mai_scurt


def meniu():
    print("Meniu:")
    print("1. Citire grafului de la tastatură")
    print("2. Cautare cel mai scurt drum între două noduri")
    print("3. Ieșire")


if __name__ == "__main__":
    def meniu():
        print("Meniu:")
        print("1. Citire grafului de la tastatură")
        print("2. Afișare matrice de adiacență")
        print("3. Cautare cel mai scurt drum între două noduri")
        print("4. Ieșire")


    if __name__ == "__main__":
        G = None
        while True:
            meniu()
            optiune = input("Alegeți o opțiune din meniu: ").strip()

            match optiune:
                case "1":
                    print("Introduceți graful orientat de la tastatură:")
                    G = citire_tastatura()
                    print("Graful citit:", G)
                case "2":
                    if G:
                        afisare_matrice_adiacenta(G)
                    else:
                        print("Graful nu a fost citit. Vă rugăm să alegeți opțiunea 1 pentru a citi graful.")
                case "3":
                    if G:
                        s = input("Introduceți nodul de start (s): ").strip()
                        t = input("Introduceți nodul țintă (t): ").strip()
                        drum_scurt = cauta_drum_cel_mai_scurt(G, s, t)
                        if drum_scurt:
                            print(f"Cel mai scurt drum între {s} și {t}: {drum_scurt}")
                        else:
                            print(f"Nu există drum între {s} și {t}.")
                    else:
                        print("Graful nu a fost citit. Vă rugăm să alegeți opțiunea 1 pentru a citi graful.")
                case "4":
                    print("Programul a fost încheiat.")
                    break
                case _:
                    print("Opțiune invalidă. Vă rugăm să introduceți o opțiune validă.")

