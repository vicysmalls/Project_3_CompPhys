from MatrixClass import*

N = int(input("How big is the matrix (NxN): N = "))
matrix = MatrixClass(N)
matrix.show()
for times in range(0, 10000000):
    row = rd.randint(0, N-1)
    col = rd.randint(0, N-1)
    matrix.checkStatus(row, col)
matrix.show()
plt.show()
