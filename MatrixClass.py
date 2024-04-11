import random as rd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

class MatrixClass:
    def __init__(self, N, amount):
        # Constant Values
        self.amount = amount
        self.N = N
        self.J = 1
        self.k = 1.38E-23
        self.T = 200
        self.matrix = []
        # Generate the Matrix
        for i in range(N):
            row = []
            for j in range(N):
                random_num = rd.randint(-1, 1)
                while random_num == 0:
                    random_num = rd.randint(-1, 1)
                row.append(random_num)
            self.matrix.append(row)
            
    # Displays the values in a matrix plot
    def show(self):
        cmap = mcolors.ListedColormap(['black', 'yellow'])
        # Plot the data
        plt.figure(figsize=(self.N, self.N))  # Adjust the figure size as needed
        plt.imshow(self.matrix, cmap=cmap, interpolation='nearest')
        plt.axis('off')  # Remove axes for a cleaner look
        plt.title(f"Graph {self.amount}: T = {self.T}")
        self.amount += 1

    # Returns: value of the cell above the input coordinates
    # Parameters: row/col of coordinate desired
    def above(self, row, col):
        if row - 1 == -1:
            return 0
        else:
            return self.matrix[row-1][col]
        
    # Returns: value of the cell below the input coordinates
    # Parameters: row/col of coordinate desired
    def below(self, row, col):
        if row + 1 == self.N:
            return 0
        else:
            return self.matrix[row+1][col]
        
    # Returns: value of the cell left of the input coordinates
    # Parameters: row/col of coordinate desired
    def left(self, row, col):
        if col - 1 == -1:
            return 0
        else:
            return self.matrix[row][col-1]

    # Returns: value of the cell right of the input coordinates
    # Parameters: row/col of coordinate desired
    def right(self, row, col):
        if col + 1 == self.N:
            return 0
        else:
            return self.matrix[row][col+1]

    # Calculates the change in energy after inverting value at input row/col
    # Returns: change in energy after flip
    # Parameters: row/col of coordinate desired
    def energyChange(self, row, col):
        total = self.above(row, col) + self.below(row, col) + self.right(row, col) + self.left(row, col)
        H_old = self.matrix[row][col] * -self.J * total  # energy before flip
        H_new = -self.matrix[row][col] * -self.J * total  # energy after flip
        delE = H_new - H_old
        return delE
    
    # Determines if 'spin' should be accepted
    # If change in energy is greater than zero or
    # exp(-deltE / kT) is greater than a random value between 0 and 1,
    # swap is enacted
    def checkStatus(self, row, col):
        delE = self.energyChange(row, col)
        if delE < 0 or np.random.rand() < np.exp(-delE/(self.k * self.T)):
            self.matrix[row][col] = -self.matrix[row][col]

     def is_equal(self, row, col, row1, col1):
        if (self.matrix[row][col] == self.matrix[row1][col1]):
            return True
        else:
            return False
