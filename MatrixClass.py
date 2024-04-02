import random as rd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
class MatrixClass:
    def __init__(self, N, amount):
        self.amount = amount
        self.N = N
        self.J = 1
        self.k = 1.38E-23
        self.T = 200
        self.matrix = []
        for i in range(N):
            row = []
            for j in range(N):
                random_num = rd.randint(-1, 1)
                while random_num == 0:
                    random_num = rd.randint(-1, 1)
                row.append(random_num)
            self.matrix.append(row)

    def show(self):
        cmap = mcolors.ListedColormap(['black', 'yellow'])
        # Plot the data
        plt.figure(figsize=(self.N, self.N))  # Adjust the figure size as needed
        plt.imshow(self.matrix, cmap=cmap, interpolation='nearest')
        plt.axis('off')  # Remove axes for a cleaner look
        plt.title(f"Graph {self.amount}: T = {self.T}")
        self.amount += 1

    # In order to know if the up,down,left,right is out of bounds,
    # row or col equals N,or -1
    def above(self, row, col):
        if row - 1 == -1:
            return 0
        else:
            return self.matrix[row-1][col]

    def below(self, row, col):
        if row + 1 == self.N:
            return 0
        else:
            return self.matrix[row+1][col]

    def left(self, row, col):
        if col - 1 == -1:
            return 0
        else:
            return self.matrix[row][col-1]

    def right(self, row, col):
        if col + 1 == self.N:
            return 0
        else:
            return self.matrix[row][col+1]

    def energyChange(self, row, col):
        total = self.above(row, col) + self.below(row, col) + self.right(row, col) + self.left(row, col)
        H_old = self.matrix[row][col] * -self.J * total  # old energy
        self.matrix[row][col] = -self.matrix[row][col]
        H_new = self.matrix[row][col] * -self.J * total  # new energy
        delE = H_new - H_old
        return delE

    def checkStatus(self, row, col):
        delE = self.energyChange(row, col)
        if delE >= 0 or np.random.rand() > np.exp(-delE/(self.k * self.T)):
            self.matrix[row][col] = -self.matrix[row][col]
