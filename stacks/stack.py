def createStack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)

def top(stack):
    return stack[len(stack)-1]

def isEmpty(stack):
    return len(stack)==0

def pop(stack):
    if not(isEmpty(stack)):
        return stack.pop()

def sortStack(A):
    B=createStack()
    while isEmpty(A) == False:
        x=top(A)
        pop(A)
        while isEmpty(B)==False and top(B)>x:
            push(A,top(B))
            pop(B)
        push(B,x)

    return B


A=[34,3,21,2,1,67]
print(sortStack(A))