'''

Question: For String s, find the longest palindromic subsequence.

Example: String = "Bananas"
:- "ana"
:- "nan"
:- "anana"

Brute Force Solution:- Check all substrings of size 1 to n... O(n^3)


Dynamic programming Solution:-
:- First and last character should match
:- Substring (excluding first & last characters) is a palindrome

0 1 2 3 4 5
| B | A | N | A | N | A |
0| B | T | F | F | F | F | F |
1| A | | T | F | T | F | T |
2| N | | | T | F | T | F |
3| A | | | | T | F | T |
4| N | | | | | T | F |
5| A | | | | | | T |



['T', 'F', 'F', 'F', 'F', 'F']
['0', 'T', 'F', 'T', 'F', 'T']
['0', '0', 'T', 'F', 'T', 'F']
['0', '0', '0', 'T', 'F', 'T']
['0', '0', '0', '0', 'T', 'F']
['0', '0', '0', '0', '0', 'T']






l = 1
[0,0] - T - B
[1,1] - T - A
[2,2] - T - N
[3,3] - T - A
[4,4] - T - N
[5,5] - T - A


l = 2

[0,1] - BA - F
[1,2] - AN - F
[2,3] - NA - F
[3,4] - AN - F
[4,5] - NA - F


l = 3
[0,2] - BAN - F
[1,3] - ANA - A&A match :- index of N=2 check [2,2] ~[start+1,end-1] if true we add T at [1,3]
[2,4] - NAN - N&N match :- T and matrix[start+1,end-1] ~ [3,3] :- T and T which is T at [2,4]
[3,5] - ANA - T

l = 4
[0,3] - BANA - F
[1,4] - ANAN - F
[2,5] - NANA - F

l = 5
[0-4] - BANAN - F
[1-5] - ANANA - A&A = T :- so T and matrix[start+1][end-1] :- T and matrix[2][4] :- T and T = T

l = 6
[0-5] - BANANA - F

'''


def LPSS(str):
    matrix = [[0 for x in range(len(str))] for y in range(len(str))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = '0'

    for i in range(len(str)):
        matrix[i][i] = 'T'



    for l in range(1,len(str)):
        start = 0
        end = l
        print(start,end)
        while end < len(str):
            val = 'F'
            print(str[start],str[end])
            if str[start] == str[end] and start + 1 == end:
                val = 'T'
            elif str[start] == str[end] and matrix[start+1][end-1] == 'T':
                val = 'T'

            matrix[start][end] = val
            start += 1
            end += 1
    printMatrix(matrix)



def printMatrix(matrix):
    for i in range(len(matrix[0])):
        print(matrix[i])



LPSS("bananas")
