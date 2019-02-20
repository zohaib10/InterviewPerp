'''
total = 11
coins: [1,5,6,8]


| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
5 | 0 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 5 | 2 | 3
6 | 0 | 1 | 2 | 3 | 4 | 1 | 1 | 2 | 3 | 4 | 2 | 2
8 | 0 | 1 | 2 | 3 | 4 | 1 | 1 | 2 | 1 | 2 | 2 | 2


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3]
[0, 1, 2, 3, 4, 1, 1, 2, 3, 4, 2, 2]
[0, 1, 2, 3, 4, 1, 1, 2, 1, 2, 2, 2]

[6, 5]

'''


def coinChanging(coins, total):
    matrix = [[0 for x in range(total + 1)] for y in range(len(coins))]
    for r in range(len(matrix)):
        for c in range(1,len(matrix[0])):
            if r == 0:
                val = c / coins[r]
                matrix[r][c] = val
            else:
                if c < coins[r]:
                    matrix[r][c] = matrix[r-1][c]
                elif c == coins[r]:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = min(matrix[r-1][c], 1 + matrix[r][c-coins[r]])
    return matrix



def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])




def traceBack(matrix, coins):
    list = []
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    val = matrix[row][col]
    while val != 0:
        if matrix[row][col] == matrix[row-1][col]:
            row -= 1
        else:
            list.append(coins[row])
            col = col - coins[row]
            row -= 1
            val = matrix[row][col]
    return list


total = 11
coins = [1,5,6,8]
matrix = coinChanging(coins, total)
list = traceBack(matrix, coins)
print(list)
