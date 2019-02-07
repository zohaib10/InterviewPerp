#Print all permutations of the list.


#This function runs through list and swaps number
def permute(nums, ind):
    if ind >= len(nums):
        print(nums)
    else:
        i = ind
        while i < len(nums):
            swap(nums, i, ind)
            permute(nums, ind + 1)
            swap(nums, i, ind)
            i+=1

# Given two indicies this swaps their values
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp



nums = [1,2,3]
permute(nums, 0)


'''
input: [1,2,3]

output: [1, 2, 3]
        [1, 3, 2]
        [2, 1, 3]
        [2, 3, 1]
        [3, 2, 1]
        [3, 1, 2]
'''
