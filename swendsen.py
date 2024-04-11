N = 20 # int(input("How big is the matrix (NxN): N = "))
matrix = MatrixClass(N, 1)
matrix.show()

loops = 1000
counter = 0
percentage = 0
for times in range(0, loops):
    # Display a progress note while running (takes ~10 minutes)
    if counter == loops/10:
        percentage += 10
        counter = 0
        print(f"{percentage}%")
    counter += 1
    
    # Pick a random coordinate within grid
    row = rd.randint(0, N-1)
    col = rd.randint(0, N-1) 
    # Swap center piece
    matrix.checkStatus(row, col)
    # Swap surrounding, connected pieces
    if (row + 1 < 20 and col + 1 < 20 and matrix.is_equal(row+1, col+1, row, col) and (matrix.is_equal(row, col+1, row, col) or matrix.is_equal(row+1, col, row, col))):
        matrix.checkStatus(row+1, col+1)
    if (row + 1 < 20 and col - 1 >= 0 and matrix.is_equal(row+1, col-1, row, col) and (matrix.is_equal(row, col-1, row, col) or matrix.is_equal(row+1, col, row, col))):
        matrix.checkStatus(row+1, col-1)
    if (col + 1 < 20 and row - 1 >= 0 and matrix.is_equal(row-1, col+1, row, col) and (matrix.is_equal(row, col+1, row, col) or matrix.is_equal(row-1, col, row, col))):
        matrix.checkStatus(row-1, col+1)
    if (row - 1 >= 0 and col - 1 >= 0 and matrix.is_equal(row-1, col-1, row, col) and (matrix.is_equal(row, col-1, row, col) or matrix.is_equal(row-1, col, row, col))):
        matrix.checkStatus(row-1, col-1)
    if (col + 1 < 20 and matrix.is_equal(row, col+1, row, col)):
        matrix.checkStatus(row, col+1)
    if (col - 1 >= 0 and matrix.is_equal(row, col-1, row, col)):
        matrix.checkStatus(row, col-1)
    if (row + 1 < 20 and matrix.is_equal(row+1, col, row, col)):
        matrix.checkStatus(row+1, col)
    if (row - 1 >= 0 and matrix.is_equal(row-1, col, row, col)):
        matrix.checkStatus(row-1, col)
    
#Display the completed swap
matrix.show()
plt.show()
