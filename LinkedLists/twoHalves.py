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
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Jan", "Feb"]
    for day in days:
        if list.headval == None:
            list.headval = Node(day)
            prevNode = list.headval
        else:
            e = Node(day)
            prevNode.nextval = e
            prevNode = e
    return list

# The Probelm: Given a LinkedList split into two halves in the middle
# This function splits a given list in half - makes two lists and prints them
def twoHalves(list):
    runner = list.headval
    head = list.headval

    while runner != None:
        head = head.nextval
        runner = runner.nextval
        if runner != None:
            runner = runner.nextval

    list1 = LinkedList()
    temp = list.headval
    while temp != head:
        if list1.headval == None:
            list1.headval = Node(temp.dataval)
            prevNode = list1.headval
        else:
            e = Node(temp.dataval)
            prevNode.nextval = e
            prevNode = e
        temp = temp.nextval

    list2 = LinkedList()
    while head != None:
        if list2.headval == None:
            list2.headval = Node(head.dataval)
            prevNode = list2.headval
        else:
            e = Node(head.dataval)
            prevNode.nextval = e
            prevNode = e
        head = head.nextval


    print("### Printing List 1 ###")
    list1.printList()
    print("### Printing List 2 ###")
    list2.printList()


# Main function calls
list1 = LinkedList()
list1 = makeList(list1)
print("### Printing Complete List ###")
list1.printList()
twoHalves(list1)


'''
"Mon" -> "Tue" -> "Wed" -> "Thu" -> "Fri" -> "Sat" -> "Sun" -> None

                                      ^
                                                                ^
Refernces:
    1. https://www.tutorialspoint.com/python/python_linked_lists.htm


Results:

### Printing Complete List ###
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Jan
Feb
### Printing List 1 ###
Mon
Tue
Wed
Thu
Fri
### Printing List 2 ###
Sat
Sun
Jan
Feb

'''
