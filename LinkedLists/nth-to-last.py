'''
Q. Given a singly Linked List, write a function to find the nth-to-last element of the list.

eg.

1 -> 2 -> 3 -> 4 -> 5 -> None

n = 2 | output: 3

Approach: Two pointer

Questions:
    1. What if n is larger than the list? 

'''


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.headVal = None


def makeList(list, vals):
    for i in range(len(vals)):
        if list.headVal == None:
            list.headVal = Node(vals[i])
            prevNode = list.headVal
        else:
            n = Node(vals[i])
            prevNode.next = n
            prevNode = n

def printList(head):
    while(head != None):
        print(head.val)
        head = head.next


linkedL = LinkedList()
list = [2,4,3,23,17,1,29,89,76]
print("Linked List")
makeList(linkedL, list)
printList(linkedL.headVal)


def nthToLast(head, n):
    curr = head 
    follower = head

    for i in range(0, n):
        if curr == None:
            return "Error: n is larger than list"
        curr = curr.next

    while curr.next != None:
        curr = curr.next
        follower = follower.next
    
    return follower.val

print("Nth to last")
print(nthToLast(linkedL.headVal, 15))