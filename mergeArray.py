#Question: Merge two sorted arrays into one sorted on. One of the array has the extra spots to merge the second into it.

#takes two lists and three pointers to keep track of where we are etc. compared elements at len1 & len2 and places the largest of the two at [length]
def mergeLists(list1, list2, len1, len2):
    len1 -= 1
    len2 -= 1
    length = len(list1) - 1
    while len1 >= 0 and len2 >= 0:
        if list1[len1] > list2[len2]:
            list1[length] = list1[len1]
            len1 -= 1
        else:
            list1[length] = list2[len2]
            len2 -= 1
        length -= 1

    if len1 < 0:
        list1[length] = list2[len2]
    print(list1)



list1 = [1,3,4,0,0,0]
list2 = [5,8,9]
len1 = 3
len2 = 3
mergeLists(list1, list2, len1, len2)


'''
input:
    list1 = [1,3,4,0,0,0]
    list2 = [5,8,9]

output:
    [1, 3, 4, 5, 8, 9]

'''
