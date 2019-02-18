'''
Question: Given a stack sort it by only using a one extra stack (ASC order)


|   |
|   |    --> Stack A
|   |
|___|


| 9 |
| 5 |   --> Stack B
| 4 |
|_3_|


1) Pop first Element from
2) Add to second stack
    i.  just push if empty
    ii. if not empty and top element is bigger than the one we have add the top elememt to old stack
        a. if not bigger we add it to our stack

'''

def sortAscending(stack1):
    stack2 = []
    while len(stack1) != 0:
        val = stack1.pop()
        if len(stack2) == 0:
            stack2.append(val)
        else:
            s2Val = stack2.pop()
            #print("val",val,"s2Val",s2Val)
            while s2Val > val:
                stack1.append(s2Val)
                if len(stack2) == 0:
                    break
                s2Val = stack2.pop()
            if s2Val < val:
                stack2.append(s2Val)
            #print("appending: ", val, " to ", stack2)
            stack2.append(val)
            #print("Stack1", stack1)
            #print("Stack2", stack2)
    return stack2

stack1 = [9,5,2,8,7,18]
print(stack1)
print(sortAscending(stack1))


'''

|   |
|   |
|   |
|   |    --> Stack A
|   |
|___|


|18 |
| 9 |
| 8 |
| 7 |    --> Stack B
| 5 |
|_2_|


Input:  [9, 5, 2, 8, 7, 18]
Output: [2, 5, 7, 8, 9, 18]



'''
