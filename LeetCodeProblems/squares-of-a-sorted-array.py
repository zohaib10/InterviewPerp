'''
A LeetCode problem:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Algorithm:
    Get the index where the negetives end and positives start
    Use two pointers one that goes through all the negetive numbers (biggest to smallest) and a second pointer which goes through all the positives (smallest to largest) and compares the squares of both and appends to new array


Time Complexity: O(N), where N is the length of A. Becuse we iterate through the list with two pointers.

Space Complexity: O(N).

'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return self.getArray(A)


    def getArray(self, A):
        j = self.getJth(A)
        i = j + 1
        lst = []
        while j >= 0 and i < len(A):
            isq = A[i] * A[i]
            jsq = A[j] * A[j]
            if isq < jsq:
                lst.append(isq)
                i += 1
            else:
                lst.append(jsq)
                j -= 1


        while j >= 0:
            lst.append(A[j] * A[j])
            j -= 1

        while i < len(A):
            lst.append(A[i] * A[i])
            i += 1


        return lst



    def getJth(self,A):
        i = 0
        while i < len(A) and A[i] <= 0:
            i += 1
        return i - 1


obj = Solution()
A = [-4,-1,0,3,10]
print(obj.sortedSquares(A))
