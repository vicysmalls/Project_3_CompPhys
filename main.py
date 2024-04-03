from MatrixClass import*
import os
amount = 1        # amount of simulations
N = 20            # size of the grid
loops = 100000000 # iterations of simulation to do
counter = 0       # used for showing progress of simulation
percentage = 0    # used for showing progress of simulation

# Create base Matrix
matrix = MatrixClass(N, amount)
matrix.show()

for times in range(0, loops):
    # Display a progress note while running (takes ~10 minutes)
    if counter == loops/100:
        percentage += 1
        counter = 0
        print(f"{percentage}%")
    counter += 1
    
    # Pick a random coordinate within grid
    row = rd.randint(0, N-1)
    col = rd.randint(0, N-1)
    # Determine if swap is necessary
    matrix.checkStatus(row, col)
#Display the completed swap
matrix.show()
plt.show()
