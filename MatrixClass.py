import random as rd


class MatrixClass:
    def __init__(self, N):
        self.N = N
        self.matrix = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(rd.randint(0, 1))
            self.matrix.append(row)

    def show(self):
        for row in self.matrix:
            print(row)

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
