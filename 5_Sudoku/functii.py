def citire_tastatura():
    sudoku = []
    for i in range(9):
        rand = [int(x) for x in input(f"Randul {i+1}: ").strip()]
        sudoku.append(rand)
    return sudoku

def citire_fisier(fisier):
    sudoku = []
    set = int(input("Setul (1 - 4): "))
    with open(fisier, "r") as f:
        linii = f.readlines()
        match(set):
            case 1:
                for linie in linii[0:9]:
                    sudoku.append(list(map(int, linie.strip().split())))
            case 2:
                for linie in linii[9:18]:
                    sudoku.append(list(map(int, linie.strip().split())))
            case 3:
                for linie in linii[18:27]:
                    sudoku.append(list(map(int, linie.strip().split())))
            case 4:
                for linie in linii[0:9]:
                    sudoku.append(list(map(int, linie.strip().split())))
    return sudoku
def afisare(sudoku):
    for rand in sudoku:
        print(*rand)

def scriere_fisier(sudoku):
    with open("out.txt", "w") as f:
        for rand in sudoku:
            f.write(' '.join(map(str, rand)) + "\n")
    print("Scriere fisier!")

