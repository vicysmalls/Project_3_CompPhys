from MatrixClass import*
import os
amount = 1

N = int(input("How big is the matrix (NxN): N = "))
matrix = MatrixClass(N, amount)
matrix.show()
loops = 1000000000
counter = 0
percentage = 0
print(f"{percentage}%")
for times in range(0, loops):
    if counter == loops/100:
        percentage += 1
        counter = 0
        print(f"{percentage}%")
    row = rd.randint(0, N-1)
    col = rd.randint(0, N-1)
    matrix.checkStatus(row, col)
    counter += 1
matrix.show()
plt.show()
