def citeste_sudoku():
    sudoku = []
    for i in range(9):
        while True:
            try:
                rand = input(f"Rândul {i + 1}: ").strip()
                rand = [int(x) for x in rand]
                if len(rand) != 9:
                    raise ValueError
                sudoku.append(rand)
                break
            except ValueError:
                print("Introduceți 9 cifre între 0 și 9. Folosiți 0 pentru spațiile goale.")

    return sudoku

def citire_fisier():
        sudoku = []
        set = int(input("Set (1 - 3) : "))
        with open("file.txt", "r") as f:
            linii = f.readlines()
        match (set):
            case 1:
                for linie in linii[0:9]:
                    sudoku.append(list(map(int, linie.strip().split())))
                return sudoku
            case 2:
                for linie in linii[9:18]:
                    sudoku.append(list(map(int, linie.strip().split())))
                return sudoku
            case 3:
                for linie in linii[18:27]:
                    sudoku.append(list(map(int, linie.strip().split())))
                return sudoku


def afiseaza_sudoku(sudoku):
    if sudoku:
        print("Tabloul Sudoku introdus este:")
        for rand in sudoku:
            print(rand)
    else:
        print("Nu există date pentru afișare.")

def scriere_fisier(sudoku):
    with open("out.txt", "w") as f:
        for linie in sudoku:
            f.write(' '.join(map(str, linie)) + "\n")
def rezolva_sudoku(mat):
    coord = [0, 0]
    if not gaseste_liber(mat, coord):
        return True  # rezolvare gata
    else:
        i, j = coord

    for nr in range(1, 10):
        if Posibil(mat, i, j, nr):
            mat[i][j] = nr
            if rezolva_sudoku(mat):
                return True
            mat[i][j] = 0

    return False


def gaseste_liber(mat, t):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                t[0], t[1] = i, j
                return True
    return False


def Posibil(mat, nlin, ncol, nr):
    return posibil_linie(mat, nlin, nr) and \
        posibil_coloana(mat, ncol, nr) and \
        posibil_caseta(mat, nlin, ncol, nr)


def posibil_linie(mat, nlin, nr):
    for j in range(9):
        if mat[nlin][j] == nr:
            return False
    return True


def posibil_coloana(mat, ncol, nr):
    for i in range(9):
        if mat[i][ncol] == nr:
            return False
    return True


def posibil_caseta(mat, nlin, ncol, nr):
    i0 = nlin - nlin % 3
    j0 = ncol - ncol % 3
    for di in range(3):
        for dj in range(3):
            if mat[i0 + di][j0 + dj] == nr:
                return False
    return True


def main():
    sudoku = None
    fis = None

    while True:
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scrierea in fisier")
        print("5. Rezolvare")
        opt = int(input("Alege: "))
        match opt:
            case 1:
                sudoku = citeste_sudoku()
            case 2:
                sudoku = citire_fisier()
            case 3:
                afiseaza_sudoku(sudoku)
            case 4:
                scriere_fisier(sudoku)
            case 5:
                if sudoku:
                    if rezolva_sudoku(sudoku):
                        print("Solutia:")
                        for rand in sudoku:
                            print(rand)
                    else:
                        print("Nu s-a găsit nicio soluție.")
                else:
                    print("Nu există date pentru rezolvare.")
            case _:
                print("Opțiune invalidă.")

if __name__ == "__main__":
    main()