import sys

class MinStack:
    def push(self, x):
        if x < self.curr_min:
            self.stack.append(2*x-self.curr_min)
            self.curr_min=x
        else:
            self.stack.append(x)
            self.curr_min = min(self.curr_min,x)

    def pop(self):
        if len(self.stack)!=0:
            if  self.stack[-1] < self.curr_min:
                self.curr_min = 2*self.curr_min-self.stack[-1]
            self.stack.pop()

    def top(self):
        if len(self.stack)==0:
            return -1
        if self.stack[-1]< self.curr_min:
            return self.curr_min
        else:
            return self.stack[-1]

    def getMin(self):
        if len(self.stack)==0:
            self.curr_min = sys.maxsize
            return -1
        return self.curr_min

    def __init__(self):
        self.stack = []
        self.curr_min = sys.maxsize
