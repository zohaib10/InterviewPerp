class QuickSort:
    def __init__(self, list):
        self.sortArray = list 

    def getArray(self):
        return self.sortArray

    def sort(self, lo, hi):
        if lo < hi:
            j = self.partition(lo, hi)
            print(j, hi)
            self.sort(lo, j)
            self.sort(j + 1, hi)

    def partition(self, lo, hi):
        pivot = self.sortArray[lo]
        i = lo + 1
        j = hi
        
        print(pivot, self.sortArray)
        print("i ", i)
        print("j ", j)
        print(self.sortArray[i] )
        while i < j:
            while self.sortArray[i] <= pivot and i < j:
                # print("HERE")
                i = i + 1
            while self.sortArray[j] > pivot:
                j = j - 1
            if i < j:
                # print("Swapping")
                self.swap(i, j)
        self.swap(lo, j)
        return j
            
    def swap(self, i, j):
        temp = self.sortArray[i]
        self.sortArray[i] = self.sortArray[j]
        self.sortArray[j] = temp