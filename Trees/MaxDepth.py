from Implementation.BinaryTree import Node


n = Node(18)
n.insert(13)
n.insert(23)
n.insert(33)
n.insert(1)
n.insert(28)

# n.postOrder()


'''
        18
    13      23
  1            33
           28


Meets base case here and we start popping from the stack
root 28   | 1 + max(dfs(None), dfs(None)) <- 4th stack
root 33   | 1 + max(dfs(None), dfs(28)) <- 3rd stack
root 23   | 1 + max(dfs(33), dfs(None)) <- 2nd stack
root: 18  | 1 + max(dfs(23), dfs(13))   <- 1st recursive stack  (Right Tree - Going up ^)

Meets base case here and we start popping from the stack
root: 18  | 1 + max(dfs(None), dfs(None))   <- 3rd recursive stack 
root: 18  | 1 + max(dfs(None), dfs(1))   <- 2nd recursive stack 
root: 18  | 1 + max(dfs(23), dfs(13))   <- 1st recursive stack  (Left Tree - Going up ^)



root 28   | 1 + max(0, 0) <- 4th stack  (Right Tree - Going down)
root 33   | 1 + max(0, 1) <- 3rd stack
root 23   | 1 + max(2, 0) <- 2nd stack
root: 18  | 1 + max(3, dfs(13))   <- 1st recursive stack  


root: 18  | 1 + max(0, 0)   <- 3rd recursive stack (Left Tree - Going down)
root: 18  | 1 + max(0, 1)   <- 2nd recursive stack 
root: 18  | 1 + max(dfs(23), 2)   <- 1st recursive stack  

root: 18  | 1 + max(3, 2) 

return 1 + 3 = 4
'''

#DFS recursive
def dfs(root):
    if root == None:
        return 0
    print(root.val)
    return 1 + max(dfs(root.right), dfs(root.left))


print("DFS Recursive ", dfs(n))