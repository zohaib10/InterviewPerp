#Question: Reverse a Stack using nothing but the given stack
def revserStack(stack):
    val = ''
    if len(stack) != 0:
        val = stack.pop()
        revserStack(stack)
    addValue(stack, val)

def addValue(stack,val):
    if len(val) == 0:
        return
    nval = ''
    if len(stack) == 0:
        stack.append(val)
    else:
        nval = stack.pop()
        addValue(stack,val)
    if len(nval) > 0:
        stack.append(nval)






stack = ["Yu Yu Hakushu", "Dragon Ball Z", "Hunter X Hunter", "Full Metal Alchemist", "Death Note", "Rurouni Kenshin"]
print(stack)
revserStack(stack)
print(stack)



'''
| 1 |
| 3 |
| 5 |
|_4_|


1) pull everything off the stack and when its empty
2) add the first from the recrsive stack which would be 4
3) when adding next which is 5 we pop off 4 and add 5 and then 4


Input:  ['Yu Yu Hakushu', 'Dragon Ball Z', 'Hunter X Hunter', 'Full Metal Alchemist', 'Death Note', 'Rurouni Kenshin']
Output: ['Rurouni Kenshin', 'Death Note', 'Full Metal Alchemist', 'Hunter X Hunter', 'Dragon Ball Z', 'Yu Yu Hakushu']


'''
