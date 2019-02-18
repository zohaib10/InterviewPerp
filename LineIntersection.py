'''
Question: Given two lines: write a function to determine if they intercept.

Refernces: Classes: https://docs.python.org/3/tutorial/classes.html

'''


class Line:
    def __init__(self, slope, yIntercept):
        self.slope = slope
        self.yIntercept = yIntercept

    def print(self):
        print("y = ", self.slope,"x +", self.yIntercept)


    def intercepts(self, line):
        if abs(self.slope) == abs(line.slope) and self.yIntercept != line.yIntercept:
            return False
        return True


line1 = Line(-13,5)
line1.print()
line2 = Line(13,3)
line2.print()

if line1.intercepts(line2):
    print("The two Lines intercept")
else:
    print("The two Lines do not intercept")

'''
Input:
    y =  3 x + 5
    y =  3 x + 3
Output:
    The two Lines do not intercept


Input:
    y =  -13 x + 5
    y =  -13 x + 3
Output:
    The two Lines do not intercept


'''
