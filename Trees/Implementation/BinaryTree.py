class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, val):
        if self.val:
            if val < self.val:
                #insert left
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                #insert right
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def preOrder(self):
        print(self.val)
        if self.left != None:
            self.left.preOrder()
        if self.right != None:
            self.right.preOrder()

    def postOrder(self):
        if self.left != None:
            self.left.postOrder()
        if self.right != None:
            self.right.postOrder()
        print(self.val)
    
    def inOrder(self):
        if self.left != None:
            self.left.inOrder()
        print(self.val)
        if self.right != None:
            self.right.inOrder() 
