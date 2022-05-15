#reference
# 1. https://www.algoexpert.io/questions/Two%20Number%20Sum
# 2. https://www.youtube.com/watch?v=nmhjrI-aW5o Bubble Sort
# 3. (a) https://www.youtube.com/watch?v=7h1s2SojIRw Quick Sort
# 4. (b) https://www.youtube.com/watch?v=-qOVVRIZzao Quick Sort Analysis

#Should Import it in from a different file
class BubbleSort: 
    def __init__(self, list):
        self.array = list 
        self.len = len(list)

    def getArray(self):
        return self.array
    
    def sort(self):
        for i in range(self.len - 1):
            j = 0
            while j < self.len - i - 1:
                if self.array[j]  > self.array[j + 1]:
                    self.swap(j, j+1)
                j = j + 1
              
    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp


def twoNumberSum(type, array, targetSum):
    # Write your code here.
    if type == 'loop':
        return loop(array, targetSum)
    elif type == 'table':
        return table(array, targetSum)
    elif type == 'pointer':
        return pointer(array, targetSum)
	
def table(array, targetSum):
    #time: O(n) worst case
    #space O(n)
    dict = {}
    for x in array:
        y = targetSum - x
        if y in dict:
            return [x, y]
        else:
            dict[x] = True
    return []

def loop(array, targetSum):
    #time: O(n^2) worst case
    #space O(1)
    for i in range(len(array)):
        j = i + 1
        while j < len(array):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
            j = j + 1		
    return []

def pointer(array, targetSum):
    #using bubble sort but ideally be using mergeSort or quickSort (quickSort with best case only)

    #time: O(n^2) with Bubble Sort
    #time O(nlogn) with Merge Sort

    #space O(1)
    bs = BubbleSort(array)
    bs.sort()
    array = bs.getArray()
    
    i = 0
    j = len(array) - 1
    while i < j:
        total = array[i] + array[j]
        if total == targetSum:
            return [array[i], array[j]]
        elif total < targetSum:
            i = i + 1
        else:
            j = j - 1


array = [3, 5, -4, 8, 11, 1, -1, 6]
sum=10
print(twoNumberSum("pointer", array, sum))



