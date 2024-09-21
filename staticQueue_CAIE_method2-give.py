"""
method 2: static circular queue follow CAIE's style using global variables
not using length or count to record valid items number
empty condition is same as full condtion
(tailPtr+1)%MAXNUM == headPtr
hints:
so need empty the location when deQueue
"""
""" init an empty queue with MAXNUM locations"""
MAXNUM = 8

queue = ["" for i in range(MAXNUM)]

# headPtr= ??
# tailPtr = ??

headPtr=0
tailPtr=-1

# FUNCTION isFull() RETURNS BOOLEAN
def isFull() -> bool:
    global MAXNUM, headPtr
    for i in range(MAXNUM):
        if queue[i]=="":
            return False
    return True

# FUNCTION isEmpty() RETURNS BOOLEAN
def isEmpty() -> bool:
    global MAXNUM, headPtr
    if queue[headPtr]=="" and (tailPtr+1)%MAXNUM == headPtr:
        return True
    return False


# FUNCTION EnQueue(BYVALUE NewItem:STRING) RETURNS BOOLEAN

def enQueue(item: str) -> bool:
    global tailPtr, MAXNUM
    if isFull():
        print("The queue is full")
        return False
    else:
        tailPtr=(tailPtr+1)%MAXNUM
        queue[tailPtr]=item
        return True



# remove an item from the front of the queue
# if queue is emtpy return an empty string
# FUNCTION DeQueue()  RETURNS  STRING
def deQueue() -> str:
    global headPtr, MAXNUM
    if isEmpty():
        print("The queue is empty")
        return ""
    else:
        item=queue[headPtr]
        queue[headPtr]=""
        headPtr=(headPtr+1)%MAXNUM
        return item


# print all queue items, from head to tail
def printAll() -> None:
    global MAXNUM, headPtr, tailPtr
    for i in range(MAXNUM):
        print(queue[i],end=" ")


if __name__ == '__main__':
    testData = [i for i in range(MAXNUM + 1)]
    print("**** push ****")
    # pushing testing
    for item in testData:
        enQueue(item)
        # print("queue=", queue)
        printAll()
        print()
    print("**** pop ****")
    # popping testing
    for i in range(MAXNUM + 1):
        item = deQueue()
        print(item, end=" ")
    print()