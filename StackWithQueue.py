#Create a Stack using Queues. Implement push() & pop() operations.
from queue import Queue

class StackWithQueue:

    def __init__(self):
        self.q = Queue()

    def push(self,val):
        if self.q.empty():
            self.q.put(val)
        else:
            nq = Queue()
            nq.put(val)
            while not self.q.empty():
                nq.put(self.q.get())
            while not nq.empty():
                self.q.put(nq.get())


    def printQueue(self):
        nq = Queue();
        while not self.q.empty():
            val = self.q.get()
            print(val)
            nq.put(val)
        while not nq.empty():
            self.q.put(nq.get())


    def pop(self):
        if self.q.empty():
            print("Stack is Empty")
        else:
            self.q.get()

stack = StackWithQueue()
stack.push(2)
stack.push(5)
stack.push(14)
stack.printQueue()
stack.pop()
print("########")
stack.printQueue()
stack.pop()
print("########")
stack.printQueue()
stack.pop()
print("########")
stack.printQueue()
stack.pop()

'''


----------
1
----------

----------
2,1
----------

Algorithm:
    Make a seperare queue to transfer the value being pushed and all the values of the exisiting queue
    Then dequeue all values from second queue to the main queue to gaurantee a fast pop operation

'''
