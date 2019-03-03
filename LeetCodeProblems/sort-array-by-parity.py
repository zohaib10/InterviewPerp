'''
Question:
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

Algorithm:
    1. I used two pointers (left & right) compared element at left with element at right and swapped them if they needed to be swapped. for example: if lst[left] is off & lst[right] is even
    2. Then I have a check to see if lst[left] is even if so I increment it. and vice versa for right

input:  [3, 1, 2, 4, 7, 9, 12, 8]
output: [8, 12, 2, 4, 7, 9, 1, 3]

'''


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1
        while left < right:
            if A[left] % 2 == 1 and A[right] % 2 == 0:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
            if A[left] % 2 == 0:
                left += 1
            if A[right] % 2 == 1:
                right -= 1
        return A

obj = Solution()
A = [3,1,2,4,7,9,12,8]
print(obj.sortArrayByParity(A))
