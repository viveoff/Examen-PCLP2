# Initial global variables
x0, y0 = 1, 1
cote = []
cale = []
n = 0

# Function to read input from the keyboard
def citire_tastatura():
    global cote, cale, n, x0, y0
    n = int(input("n = "))
    cote = n * [None]
    cale = n * [None]
    for i in range(n):
        cote[i] = [int(x) for x in input("Cote (0,0,0): ").split()]
        cale[i] = [0] * n
    x0 = int(input("x0 = "))
    y0 = int(input("y0 = "))

# Function to display the input data
def afisare_date():
    print(f"Coordonate initiale: {x0}, {y0}")
    for i in range(n):
        print(*cote[i])

# Function to write data to a file
def scriere_fisier():
    with open("out.txt", "w") as f:
        f.write(f"{x0}, {y0}\n")
        for lin in cote:
            f.write(' '.join(map(str, lin)) + "\n")

# Function to read data from a file
def citire_fisier():
    global cote, cale, x0, y0, n
    with open("file.txt", "r") as f:
        linii = f.readlines()
        set = int(input("Set: "))
        match set:
            case 1:
                n = int(linii[0])
                cote = [None] * n
                cale = [None] * n
                for i in range(n):
                    cote[i] = [int(x) for x in linii[i+1].strip().split()]
                    cale[i] = [0] * n
                x0 = int(linii[4])
                y0 = int(linii[5])
                print("Citire fisier!")
            case 2:
                n = int(linii[6])
                cote = [None] * n
                cale = [None] * n
                for i in range(n):
                    cote[i] = [int(x) for x in linii[i+1].strip().split()]
                    cale[i] = [0] * n
                x0 = int(linii[10])
                y0 = int(linii[11])
                print("Citire fisier!")

# Function to find the path using backtracking
def cautaCale(k, x, y):
    global n, cale
    if peMargine(x, y):
        afisareSolutie()
    for i in range(4):
        xn = x + dx[i]
        yn = y + dy[i]
        if not inAfaraZonei(xn, yn) and Posibil(x, y, xn, yn):
            cale[xn][yn] = k
            cautaCale(k + 1, xn, yn)
            cale[xn][yn] = 0

# Function to check if a move is possible
def Posibil(x, y, xn, yn):
    global cote, cale
    return cote[x][y] > cote[xn][yn]

# Function to check if a position is on the border
def peMargine(x, y):
    global n
    return x == 0 or x == n - 1 or y == 0 or y == n - 1

# Function to check if a position is out of bounds
def inAfaraZonei(xn, yn):
    global n
    return xn < 0 or xn >= n or yn < 0 or yn >= n

# Function to display the solution
def afisareSolutie():
    global n, cale, nr_solutie
    nr_solutie += 1
    print(f"Solutia {nr_solutie}:")
    afisareMatrice(cale)

# Function to display a matrix
def afisareMatrice(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]:2}", end=" ")
        print()

# Directions for moving in the grid (up, right, down, left)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Function to solve the problem
def rezolvare():
    global nr_solutie
    nr_solutie = 0
    cautaCale(1, x0, y0)

