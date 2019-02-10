'''

Total weight: 7

items

1 | 1
3 | 4
4 | 5
5 | 7


__|_0_|_1_|_2_|_3_|_4_|_5_|_6_|_7_|
1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
3 | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
4 | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
5 | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

- to calculate
    :- check max weight allowed and if that column weight is equal to max then input its val
    :- if wight is greater than column - then check prev row

- To trace back
    :- we start at [i,j]
    :- if [i,j] > [i-1,j] then subtract the weight of row and move up --i
    :- else move up
    :- repeat until you get to 0
'''
from __future__ import print_function


def kanpsack(dict, weight):
    print(dict)
    matrix = [[0 for x in range(weight + 1)] for y in range(len(dict))]
    keyMap = {}
    i = 0
    for key, value in dict.iteritems():
        keyMap[i] = key
        i+=1
    #print(keyMap)
    for row in range(len(dict)):
        for column in range(0,weight+1):
            if column == 0:
                matrix[row][column] = 0
            else:
                colVal = 0
                if column  < keyMap.get(row):
                    if row > 0:
                        colVal = matrix[row-1][column]
                else:
                    colVal = dict.get(keyMap.get(row))
                    if column > keyMap.get(row) and row > 0:
                        colInd = column - keyMap.get(row)
                        colVal = colVal + matrix[row-1][colInd]
                    if row > 0:
                        colVal = max(colVal,matrix[row-1][column])
                matrix[row][column] = colVal

    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], "  |  ", end= '')
        print()

def findVals(matrix):
    row = len(matrix) -1
    col = len(matrix[0]) -1
    val = matrix[row][col]
    list = []
    while val != 0:
        if val == matrix[row-1][col]:
            row -= 1
        else:
            subVal = matrix[row][col] - matrix[row-1][col]
            col = col - subVal
            val = matrix[row][col]
            list.append(subVal)
    return list


dict = {1:1,3:4,4:5,5:7}
matrix = kanpsack(dict, 7)
printMatrix(matrix)
print(findVals(matrix))


'''

Output: knapsack function
{1: 1, 3: 4, 4: 5, 5: 7}
0   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |
0   |  1   |  1   |  4   |  5   |  5   |  5   |  5   |
0   |  1   |  1   |  4   |  5   |  6   |  6   |  9   |
0   |  1   |  1   |  4   |  5   |  7   |  8   |  9   |


findVals Logic:-
subVal = 9 - 5 = 4
col = 7 - 4 = 3
val = [2][3] = 4
list = [4]

subVal = 4 - 1 = 3
col = 3 - 3 = 0
val = [0][1] = 0
list = [4,3]

Output: knapsack & findVals:-
{1: 1, 3: 4, 4: 5, 5: 7}
0   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |
0   |  1   |  1   |  4   |  5   |  5   |  5   |  5   |
0   |  1   |  1   |  4   |  5   |  6   |  6   |  9   |
0   |  1   |  1   |  4   |  5   |  7   |  8   |  9   |
[4, 3]
'''

#https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
#https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
#https://www.geeksforgeeks.org/python-dictionary/
#https://www.w3schools.com/python/python_lists.asp
