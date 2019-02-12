'''
Longest Common Subsequence

input:
    str1 = abcdaf
    str2 = acbcf

    a   b   c   d   a   f
a | 1 | 1 | 1 | 1 | 1 | 1 |
c | 1 | 1 | 2 | 2 | 2 | 2 |
b | 1 | 2 | 2 | 2 | 2 | 2 |
c | 1 | 2 | 3 | 3 | 3 | 3 |
f | 1 | 2 | 3 | 3 | 3 | 4 |


'''


from __future__ import print_function


def findCommon(str1, str2):
    matrix = [[0 for x in range(len(str2))] for y in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            val = 0
            if str1[i] != str2[j]:
                if i > 0 and j > 0:
                    val = max(matrix[i-1][j], matrix[i][j-1])
                elif i > 0 and j <= 0:
                    val = matrix[i-1][j]
                elif j > 0 and i <= 0:
                     val = matrix[i][j-1]
            else:
                val = 1
                if i > 0 and j > 0:
                    val = val + matrix[i-1][j-1]
            matrix[i][j] = val
    return matrix


def reShapeMatrix(matrix,str1):
    row = len(matrix)
    col = len(matrix[0])
    matrix1 = [[0 for x in range(col + 1)] for y in range(row + 1)]
    for r in range(1,row+1):
        for c in range(1,col+1):
            matrix1[r][c] = matrix[r-1][c-1]

    return matrix1





def findString(matrix, str1):
    matrix = reShapeMatrix(matrix,str1)
    list = []
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    val = matrix[row][col]
    while val > 0:
        if val > matrix[row-1][col] and val > matrix[row][col-1]:
            col -= 1
            row -= 1
        elif val == matrix[row-1][col] and val != matrix[row][col-1]:
            row -= 1
        else:
            col -= 1
        if val != matrix[row][col]:
            print(val)
            if val == 1:
                val -= 1
            list.append(str1[val])
            val = matrix[row][col]

    print(str1)
    printMatrix(matrix)
    return list




def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], "  |  ", end= '')
        print()



str2 = "ABCDGH"
str1 = "AEDFHR"
matrix = findCommon(str1, str2)
print(findString(matrix, str1))



'''


    A   B   C   D   G   H
A   1   1   1   1   1   1
E   1   1   1   1   1   1
D   1   1   1   2   2   2
F   1   1   1   2   2   2
H   1   1   1   2   2   3
R   1   1   1   2   2   3




'''
