import random as rd

N = int(input("How big is the matrix (NxN): N = "))
matrix = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(rd.randint(0,1))
    matrix.append(row)

for row in matrix:
    print(row)
