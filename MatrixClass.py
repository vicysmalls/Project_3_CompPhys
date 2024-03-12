import random as rd

class Matrix:
    def __init__(self, N):
        self.N = N
        self.matrix = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(rd.randint(0, 1))
            self.matrix.append(row)

    def edge(self, row, col):
        if ((row == 0) or (col == 0) or (row == self.N - 1) or (col == self.N - 1)):
            return True
        else:
            return False

    def above(self, row, col):
        

