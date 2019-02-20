'''
sumTo = 11
nums = [2,3,7,8,10]


    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
 2  | T | F | T | F | F | F | F | F | F | F | F  | F  |
 3  | T | F | T | T | F | T | F | F | F | F | F  | F  |
 7  | T | F | T | T | F | T | F | T | F | T | T  | F  |
 8  | T | F | T | T | F | T | F | T | T | T | T  | T  |
10  | T | F | T | T | F | T | F | T | T | T | T  | T  |

'''

def SubetSum(sumTo, nums):
    matrix = [[0 for x in range(sumTo + 1)] for y in range(len(nums))]
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        matrix[i][0] = 'T'

    for r in range(row):
        for c in range(1,col):
            if r == 0:
                if c == nums[r]:
                    matrix[r][c] = 'T'
                else:
                    matrix[r][c] = 'F'
            else:
                if c < nums[r]:
                    matrix[r][c] = matrix[r-1][c]
                elif c == nums[r]:
                    matrix[r][c] = 'T'
                elif matrix[r-1][c] == 'T':
                    matrix[r][c] = 'T'
                else:
                    matrix[r][c] = matrix[r-1][c-nums[r]]

    return matrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])



def traceBack(matrix, nums):
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    list = []
    while row > 0:
        if matrix[row-1][col] == 'T':
            row -= 1
        else:
            list.append(nums[row])
            col = col - nums[row]
            row -= 1
    if matrix[row][col] == 'T':
        list.append(nums[row])
    return list

sumTo = 20
nums = [2,3,7,8,10]
matrix = SubetSum(sumTo, nums)
printMatrix(matrix)
list = traceBack(matrix, nums)
print(list)

'''
sumTo = 11
nums = [2,3,7,8,10]

['T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'F', 'T', 'T', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'T', 'T', 'T']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'T', 'T', 'T']
[8, 3, 2]
'''

'''
sumTo = 20
nums = [2,3,7,8,10]

['T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'F', 'T', 'T', 'F', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'F', 'T']
['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'T', 'T']
[8, 7, 3, 2]
'''
