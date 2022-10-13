from copy import deepcopy

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        sttr = ''
        for i in range(len(self.matrix)):
            sttr = sttr + '\t'.join(map(str, self.matrix[i])) + '\n'
        return sttr

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        rst = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                rst[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(rst)


m1 = [[31, 22, 1],[37, 43, 2],[51, 86, 3]]
m2 = [[3, 5, 32],[2, 4, 6],[-1, 64, -8]]
m3 = [[3, 5, 8], [3, 8, 3], [7, 1, 5]]
m = Matrix(m1)
mm = Matrix(m2)
mmm = Matrix(m3)
print(m)
print(mm)
print(mmm)

M = m + mm + mmm
print(M)
