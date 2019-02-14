
'''
[[1,2],[2,3],[3,4]]



__|__0__|__1__|__2__
0 |  0  |  6  |  18
1 |     |  0  |  24
2 |     |     |  0


0-2:
    6 + 1*3*4 = 18
    24 + 1*2*4 = 33

'''


def mcm(list):
    dict = {}
    for i in range(len(list)):
        val = 0
        j = 0
        while j < i and i < len(list):
            if i - j <= 1:
                print(list[j], list[i], i+j)
                l1 = list[j]
                l2 = list[i]
                dict[i+j] = l1[0] * l1[1] * l2[1]
            j+=1
            i+=1
    print(dict)

list = [[1,2],[2,3],[3,4]]
mcm(list)
