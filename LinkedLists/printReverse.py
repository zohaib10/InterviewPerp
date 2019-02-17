#Question: Given a LinkedList, print it in reverse.


class Node:
    def __init__(self, dataval):
        self.nextval = None
        self.dataval = dataval


class LinkedList:
    def __init__(self):
        self.headval = None




def makeList(linkedL, list):
    for ind in range(len(list)):
        if linkedL.headval == None:
            linkedL.headval = Node(list[ind])
            prevNode = linkedL.headval
        else:
            n = Node(list[ind])
            prevNode.nextval = n
            prevNode = n

def printList(head):
    while head != None:
        print(head.dataval)
        head = head.nextval


def printReverse(head):
    if head.nextval != None:
        printReverse(head.nextval)
    print(head.dataval)


linkedL = LinkedList()
list = [2,4,3,23,17,1,29,89,76]
print("Linked List")
makeList(linkedL, list)
printList(linkedL.headval)
print("Linked List Prinited Reverse")
printReverse(linkedL.headval)

# list.headval = Node(2)
#
# n = Node(6)
# list.headval.nextval = n
# printList(list.headval)

'''

Linked List
2
4
3
23
17
1
29
89
76
Linked List Prinited Reverse
76
89
29
1
17
23
3
4
2



'''
