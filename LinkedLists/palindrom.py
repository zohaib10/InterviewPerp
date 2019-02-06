# Question :- Write a function to check if a LinkedList is a palindrome?

# This class defines each Node of the LinkedList
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


# This class defines the Linked List with a head value
class LinkedList:
    def __init__(self):
        self.headval = None

    #This function lets us print the LinkedList
    def printList(self):
        n = self.headval
        while n != None:
            print(n.dataval)
            n = n.nextval


# A function that makes the list for you given an array of values
def makeList(list):
    nums = [1,2,3,4,5,5,4,3,2,1]
    for num in nums:
        if list.headval == None:
            list.headval = Node(num)
            prevNode = list.headval
        else:
            e = Node(num)
            prevNode.nextval = e
            prevNode = e
    return list


# Function to check if list is a palindrome
def isPalindrome(list):
    head = list.headval
    runner = list.headval
    #increment runner twice as fast a head
    while runner != None:
        head = head.nextval
        runner = runner.nextval
        if runner != None:
            runner = runner.nextval

    #stack
    stack = []
    #push value of head into stack until its null
    while head != None:
        stack.append(head.dataval)
        head = head.nextval
    #pop each item from stack and compare to first half of LinkedList
    temp = list.headval
    while len(stack) > 0:
        num = stack.pop()
        if num != temp.dataval:
            return False
        temp = temp.nextval

    return True


list = LinkedList()
list = makeList(list)
#list.printList()
if isPalindrome(list):
    print("Is a Palindrome")
else:
    print("Not a Palindrome")


'''

1   2   3   4   5   5   4   3   2   1
^
^

ex: nums = [1,2,3,4,5,6,4,3,2,1]
    returns: Not a Palindrome
ex: nums = [1,2,3,4,5,5,4,3,2,1]
    returns: Is a Palindrome
ex: nums = [1,2,3,4,5,4,3,2,1]
    returns: Is a Palindrome

'''
