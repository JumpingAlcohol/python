""""
ADT Stack:
    Stack(self)         # create an empty stack
    isEmpty(self)       # decide whether the stack is empty , if it is return True else return False
    isFull(self)        #                              full
    push(self, elem)    # push elem into the top of the stack
    pop(self)           # pop element from the top of the stack and return it
    peek(self)           # return the top element in the stack but don't delete it.
"""
""" static stack """
""" method2: top pointer points to empty location above the top element """

""" pay attention:
    The top pointer points to upper free space of the top element 
    and
    the stack grows up to the large address
"""
""" pseudo for static stack
feature of stack:  FILO  / LIFO"""
# DECLARE MAXNUM :INTEGER = 10
# to be implemented
MAXNUM = 10
# DECLARE stack:ARRAY[0:MAXNUM-1] OF STRING
# to be implemented

stack=['' for i in range(MAXNUM)]

# DECLARE top :INTEGER     // point to the upper free space of the top element
# init the top poniter to init an empty stack
# to be implemented

top=0

# FUNCTION isEmpty() RETURNS BOOLEAN
def isEmpty()->bool:
    global top
    if top==0:
        return True
    return False

# FUNCTION isFull() RETURNS BOOLEAN
def isFull()->bool:
    global top
    if top==MAXNUM:
        return True
    return False

# PROCEDURE push(item:STRING)
def push(item:str)->None:
    global top
    if isFull():
        print("The stack is full")
    else:
        stack[top]=item
        top=top+1
    return None

# FUNCTION pop() RETURNS STRING   // empty stack return empty string
def pop()->str:
    global top
    if isEmpty():
        print("The stack is empty")
        return ""
    else:
        item=stack[top-1]
        top=top-1
        return item




# FUNCTION peek() RETURNS STRING  // empty stack return empty string
# return the top element but not do popping operation.
def peek()->str:
    global top
    if isEmpty():
        print("The stack is empty")
        return ""
    else:
        item=stack[top-1]
        return item

def printAll()->None: # print the stack from base to top, left is base, right is top
    for i in range(MAXNUM):
        print(stack[i],end=" ")

if __name__ == '__main__':
    testData = [ i for i in range(MAXNUM+1)]
    # pushing testing
    for item in testData:
        push(item)
        printAll()
    # popping testing
    for i in range(MAXNUM+1):
        item = pop()
        print(item , end = " ")
    print()