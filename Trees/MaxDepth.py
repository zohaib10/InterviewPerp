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
                    
'''

#DFS recursive
def dfs(root):
    if root == None:
        return 0

    return 1 + max(dfs(root.right), dfs(root.left))


print("DFS Recursive ", dfs(n))