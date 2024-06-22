concurente=[]
n=0

def Menu():
    meniu={}
    meniu['C']='citire date de la tastatura'
    meniu['F']='citire date din fisier'
    meniu['A']='afisare matrice'
    meniu['R']='rezolvare problema'
    meniu['I']='info autor'
    meniu['T']='terminare program'
    print()
    for i in meniu:
        print(i+'.'+meniu[i])
    x=input('alegeti o optiune:')
    return x

def citire_tastatura():
    global n, concurente
    n = int(input("n = "))
    concurente = []
    for i in range(n):
        concurenti_input = input(f"Concurenti a lui {i+1}: ").split()
        concurenti = [0] * n
        for c in concurenti_input:
            concurenti[int(c) - 1] = 1
        concurente.append(concurenti)
    return n, concurente




def citire_fisier():
    global n, concurente
    with open("file.txt", 'r') as file:
            n = int(file.readline().strip())
            concurente = []
            for _ in range(n):
                concurenti_input = file.readline().strip().split()
                concurenti = [0] * n
                for c in concurenti_input:
                    concurenti[int(c) - 1] = 1
                    concurente.append(concurenti)
    return n, concurente

def afisare_mat():
    for i in range(n):
        print(*concurente[i])

fis=open('file.txt','r')

def MasaRotunda(k):
    global asezat,n,mr
    if k >= n:
        afisSolutie()
    else:
        for i in range(n):
            if asezat[i] == False and Posibil(i,k):
                asezat[i] = True
                mr[k] = i
                MasaRotunda(k+1)
                asezat[i] = False

def Posibil(i,k):
    global concurente,mr,n
    if k > 0 and concurente[mr[k-1]][i] != 0:
        return False
    if k == n-1 and concurente[mr[0]][i] != 0:
        return False
    return True

def afisSolutie():
    global mr,nrsol
    nrsol = nrsol + 1
    print("solutia",nrsol,"mr=",mr)

m = 0
while True:
    opt = Menu()
    if opt == 'C':
        n, concurente = citire_tastatura()
    if opt == 'F':
        n, concurente = citire_fisier(fis)
    if opt == 'A':
        afisare_mat()
    if opt == 'R':
        asezat = [False] * n
        mr = [0] * n
        nrsol = 0
        MasaRotunda(0)
        if nrsol == 0:
            print("nu exista solutie")
        afisSolutie()
    if opt == 'T':
        break
