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


def findString(matrix, str1):
    printMatrix(matrix)
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    val = matrix[row][col]
    list = []
    while val > 0:
        if row > 0 and col > 0:
            if val > matrix[row-1][col] and val > matrix[row][col-1]:
                list.append(str1[col-1])
                row -= 1
                col -= 1
            elif val > matrix[row-1][col]:
                row -= 1
            else:
                col -= 1
            val = matrix[row][col]
        else:
            if matrix[row][col] == 1:
                list.append(str1[col-1])
                val = 0
    return list

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], "  |  ", end= '')
        print()



str2 = "abcdaf"
str1 = "acbcf"
matrix = findCommon(str1, str2)
print(findString(matrix, str1))
