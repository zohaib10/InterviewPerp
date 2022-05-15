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
              
    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp