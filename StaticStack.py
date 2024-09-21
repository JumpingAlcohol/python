"""
Stack is a FIFO / LIFO ADT

ADT Stack:
    Stack(self)         # create an empty stack
    isEmpty(self)       # decide whether the stack is empty , if it is return True else return False
    isFull(self)        #                              full
    push(self, elem)    # push elem into the top of the stack
    pop(self)           # pop element from the top of the stack and return it
    peek(self)           # return the top element in the stack but don't delete it.


"""

""" static stack """

""" method1:  provide by CAIE's course book  Hodder's p464 """

""" pay attention:
    The top pointer points to the top element 
    and
    the stack grows up to the large address
"""

"""
pseudo:

DECLARE MAXNUM = 100
DECLARE  stack:ARRAY[0:MAXNUM-1] OF STRING

DECLARE  top :INTEGER  # point to the top element in stack

PROCEDURE InitStack()  #empty stack

FUNCTION isFull() RETURNS BOOLEAN 

FUNCTION isEmpty() RETURNS BOOLEAN 

FUNCTION push( BYVALUE item :STRING) RETURNS BOOLEAN

FUNCTION pop() RETURNS STRING  //if empty return ""

FUNCTION peek() RETURNS STRING  // if empty return ""
"""
"""  declare an integer constant named as MAXNUM  """
# DECLARE MAXNUM = 100
MAXNUM = 100

"""  declare a stack space which can include maxmize 100 string in it."""
# DECLARE  stack:ARRAY[0:MAXNUM-1] OF STRING
stack = ["" for index in range(MAXNUM)]

""" declare the top pointer of the stack which point to the top element in the stack   """
# DECLRAE top :INTEGER
top = -1


''' init empty stack '''
def initStack():
    global top
    top = -1

''' if stack is empty return True else return False'''
def isEmpty()->bool:
    global top
    if top == -1:
        return True
    else:
        return False

''' if stack is full return True else return False'''
def isFull()->bool:
    global top
    if top == MAXNUM-1:
        return True
    else:
        return False

''' push an element into the top of the stack, if stack is full give proper message to user'''
def push(elem:str)->None:
    global top
    if isFull():
        print("Full")
        return None
    top=top+1
    stack[top]=elem

""" pop the top element of the stack and return the element, if stack is empty return empty string """
def pop()->str:
    global top
    if isEmpty():
        return "Empty"
    item=stack[top]
    top=top-1
    return item

''' return the top element but not pop it, if the stack is empty return empty string'''
def peek()->str:
    global top
    if isEmpty():
        return "Empty"
    return stack[top]


''' print all valid element in the sack from top to base.    left end is base , right end is top'''
def printAll()->None:
    global top
    for i in range(top+1):
        print(stack[i],end=" ")


""" testing """
if __name__ == "__main__":
    """ create an empty stack """
    initStack()

    """ push item in testData one by one : testData=[3,5,7,10,12] """
    testData=["google","baidu","apple","huawei","microsoft","chatGPT"]
    for item in testData:
        print(f"pushing ... {item} in.")
        push(item)
        printAll()
        print()



    """ pop items out from the stack """
    for i in range(6):
        item=pop()
        if item:
            print(f"pop out ... {item}.")
        printAll()
        print()