N = 20
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
    # Determine if swap is necessary
    matrix.checkStatus(row, col)
    if (row + 1 < 20 and col + 1 < 20):
        matrix.checkStatus(row+1, col+1)
    if (row + 1 < 20 and col - 1 >= 0):
        matrix.checkStatus(row+1, col-1)
    if (col + 1 < 20 and row - 1 >= 0):
        matrix.checkStatus(row-1, col+1)
    if (row - 1 >= 0 and col - 1 >= 0):
        matrix.checkStatus(row-1, col-1)
    
#Display the completed swap
matrix.show()
plt.show()
