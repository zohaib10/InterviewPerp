'''
Question: Logest Palindromic Subsequence


str = "agbdba"

1) make a matrix of size len X len
2) go to the string by length

l = 1
0-0,1-1,2-2,3-3,4-4,5-5

l=1
0-1,1-2,2-3,3-4,4-5
ag , gb, bd, db,ba


l=2
0-2, 1-3, 2-4, 3-5
agb, gbd, bdb, dba

l=3
0-3,   1-4,   2-5,
agbd   gbdb   bdba

l=4
0-4     1-5
agbdb   gbdba


l=5
agbdba


   | 0 | 1 | 2 | 3 | 4 | 5 |
 0 | 1 | 1 | 1 | 1 | 3 | 5 |
 1 | 0 | 1 | 1 | 1 | 3 | 3 |
 2 | 0 | 0 | 1 | 1 | 3 | 3 |
 3 | 0 | 0 | 0 | 1 | 1 | 1 |
 4 | 0 | 0 | 0 | 0 | 1 | 1 |
 5 | 0 | 0 | 0 | 0 | 0 | 1 |


[1, 1, 1, 1, 1, 3]
[0, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 3, 3]
[0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 1]



'''


def LPS_Matrix(str):
    matrix = [[0 for x in range(len(str))] for y in range(len(str))]

    for l in range(len(str)):
        r = 0
        c = l
        print("Length:",l)
        while c < len(str):

            val = 1

            if str[r] == str[c]:
                if r != c:
                    val = 2 + matrix[r+1][c-1]
            else:
                val = max(matrix[r-1][c], matrix[r][c-1])
            matrix[r][c] = val
            print("r,c",r,c)
            print("val", val)
            c+=1
            r+=1
    printMatrix(matrix)



def printMatrix(matrix):
    for i in range(len(matrix[0])):
        print(matrix[i])





str = "agbdba"
LPS_Matrix(str)
