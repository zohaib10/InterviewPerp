'''
str1 = "abcdef"
str2 = "azced"

{'d to c': 'Conversion', 'f to d': 'Conversion', 'b': 'Deleted', 'c to z': 'Conversion'}


'''
def minimumEditDistance(str1, str2):
    #print(len(str1), len(str2))
    matrix = [[0 for x in range(len(str1) + 1)] for y in range(len(str2)+1)]
    #printMatrix(matrix)
    matrix = initCol(matrix)
    matrix = initRow(matrix)
    #printMatrix(matrix)

    for r in range(1,len(matrix)):
        for c in range(1,len(matrix[0])):
            val = 0
            if str1[c-1] == str2[r-1]:
                val = min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1])
            else:
                val = min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1]) + 1
    return matrix


def initRow(matrix):
    for j in range(len(matrix[0])):
        matrix[0][j] = j
    return matrix

def initCol(matrix):
    for i in range(len(matrix)):
        matrix[i][0] = i
    return matrix



def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def traceBack(matrix, str1, str2):
    r = len(matrix)-1
    c = len(matrix[0])-1
    dict = {}
    #print(str1[c-1], str2[r-1])
    while c > 0 and r > 0:
        if matrix[r-1][c-1] == min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1]):
            r -= 1
            c -= 1
            if str1[c] != str2[r]:
                dict[str1[c] + ' to ' + str2[r]] = 'Conversion'
        elif matrix[r-1][c] == min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1]):
            r -= 1
            dict[str2[r]] = "Added"
        else:
            c -= 1
            dict[str1[c]] = 'Deleted'

    return dict


str1 = "abcdef"
str2 = "azced"
matrix = minimumEditDistance(str1, str2)
print("Total number of Operations: ", matrix[len(matrix)-1][len(matrix[0])-1])
dict = traceBack(matrix, str1, str2)
print(dict)
