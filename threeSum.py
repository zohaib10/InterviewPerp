#Given a list of integers, write a function that retuens all sets of 3 numbers in the list, a b and, c so that a + b + c = 0.


def threeSum(list):
    list = insertionSort(list)
    print(list)
    first = 0
    while first < len(list):
        second = first + 1
        third = len(list) - 1
        while second < third:
            if list[first] + list[second] + list[third] == 0:
                return [list[first], list[second], list[third]]
            elif list[first] + list[second] + list[third] < 0:
                second += 1
            else:
                third -= 1
        first += 1
    return [None, None, None]

def insertionSort(list):
    i = 0
    while i < len(list):
        j = i
        while j > 0 and list[j-1] > list[j]:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j-=1
        i+=1
    return list



list = [-1, 0, 1, 2, 4, -4]
list1 = threeSum(list)
print(list1)


'''

list = [-1, 0, 1, 2, -1, -4]

sort list
list = [-4, -1, -1, 0, 1, 2]

[-4, -1, -1, 0, 1, 2]
  ^
                ^^
-4 + -1 + 2 = -3 less than 0 so increment 2nd pointer
-4 + -1 + 2 = -3 less than 0 so increment 2nd pointer
-4 + 0 + 2 = -2  less than 0 so increment 2nd pointer
-4 + 1 + 2 = 1   greater than 0 decrement 3rd pointer
if same move to next iteration of loop

increment first pointer
[-4, -1, -1, 0, 1, 2]
      ^
          ^
                   ^
-1 + -1 + 2 = 0 Found so return


input:[-1, 0, 1, 2, -1, -4]
output: [-1, -1, 2]

input:[-1, 0, 1, 2, -2, -4]
output: [-2, -0, 2]

'''
