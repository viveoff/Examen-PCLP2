fis = None
def citire_tastatura():
  global n,spec_date, spectacole
  spec_date = []
  spectacole = []
  n = int(input("Nr de spectacole: "))
  for i in range(n):
      start = input("Start HH:MM : ")
      end = input("Sfarsit HH:MM : ")
      ore_start, min_start = map(int, start.strip().split(":"))
      ore_end, min_end = map(int, end.strip().split(":"))
      spec_date.append((ore_start, min_start, ore_end, min_end))
      spectacole.append((ore_start * 60 + min_start, ore_end * 60 + min_end))


def afisare():
    global n,spec_date, spectacole
    print("Nr de spectacole: ",n)
    for i in range(n):
        ore_start, min_start, ore_end, min_end = spec_date[i]
        print(f"Spectacolul {i+1}: {ore_start:02d}:{min_start:02d} - {ore_end:02d}:{min_end:02d}")

def scriere_fisier():
    global spec_date
    with open("out.txt", "w") as f:
        for start_time in spec_date:
            start_str = f"{start_time[0]}:{start_time[1]}"
            end_str = f"{start_time[2]}:{start_time[3]}"
            f.write(f"{start_str} {end_str}\n")

def citire_fisier(fis):
    global bancnote_disponibile
    try:
        # Citește numărul de bancnote
        line = fis.readline().strip()
        if not line:  # Verifică dacă am ajuns la sfârșitul fișierului
            return False

        n = int(line)
        bancnote_disponibile = []
        for _ in range(n):
            line = fis.readline().strip()
            if not line:  # Verifică dacă am ajuns la sfârșitul fișierului
                return False
            valoare_bancnota, cantitate_bancnota = map(int, line.split())
            bancnote_disponibile.append((valoare_bancnota, cantitate_bancnota))
        print("Citire din fisier cu succes")
        return True
    except Exception as e:
        print("Eroare la citirea din fișier:", e)
        return False

def rezolvare():
    global spectacole

    # Sortăm spectacolele după ora de finalizare
    spectacole.sort(key=lambda x: x[1])

    # Lista pentru a ține evidența spectacolelor selectate
    spectacole_selectate = []

    # Ultima oră de finalizare considerată
    ora_ultima_selectata = -1

    for spectacol in spectacole:
        start, end = spectacol
        if start >= ora_ultima_selectata:
            spectacole_selectate.append(spectacol)
            ora_ultima_selectata = end

    # Afișăm spectacolele selectate
    print("Spectacole selectate pentru vizionare:")
    for spectacol in spectacole_selectate:
        ore_start, min_start = divmod(spectacol[0], 60)
        ore_end, min_end = divmod(spectacol[1], 60)
        print(f"{ore_start:02d}:{min_start:02d} - {ore_end:02d}:{min_end:02d}")
