"""
method 1: static circular queue follow CAIE's style using global variables
"""
"""   
TOPIC FOUR: STATIC QUEUE PSEUDO CODE

//NullPointer should be set to -1 if using array element with index 0
CONSTANT EMPTYSTRING=“”
CONSTANT NullPointer = -1
CONSTANT MaxQueueSize = 8
DECLARE FrontPoint : INTEGER    # point to the head element
DECLARE TailPoint : INTEGER     # point to the tail element
DECLARE Count : INTEGER
DECLARE Queue : ARRAY[0: MaxQueueSize - 1] OF STRING

PROCEDURE InitialiseQueue ( )
   FrontPoint <-- 0
   TailPoint <-- -1
   Count <-- 0
ENDPROCEDURE

// isFull
FUNCTION isFull() RETURNS BOOLEAN
  RETURN Count = MaxQueueSize
ENDFUNCTION

FUNCTION isEmpty() RETURNS BOOLEAN
  RETURN Count = 0

ENDFUNCTION


// add one item at the end of the queue
FUNCTION EnQueue(BYVALUE NewItem:STRING) RETURNS BOOLEAN
   IF isFull()
       THEN
           RETURN FALSE
       ELSE
           TailPtr <-- ( TailPtr+1) MOD MaxQueueSize
           Queue[TailPtr]<--NewItem
           Count <-- Count + 1
           RETRUN TRUE
    ENDIF
ENDFUNCTIOM


//remove an item from the front of the queue
// if queue is emtpy return an empty string
FUNCTION DeQueue()  RETURNS  STRING


ENDFUNCTION

"""
""" define a circular queue 
    FIFO
    frontPtr points to the first element in the queue
    tailPtr  points to the last element                 
    count   the valid elements number in the queue
"""


limit = 100
Queue = [None for i in range(limit)]            #0 -- limit -1

""" initialize empty queue """
frontPtr = 0
tailPtr = -1
count = 0

def isEmpty():
    global count
    return count==0

def isFull():
    global count
    return count==limit

def enQueue(item):
    global count,tailPtr
    if isFull():
        print("Full")
        return False
    count=count+1
    tailPtr=(tailPtr+1)%limit
    Queue[tailPtr]=item
    return True


def deQueue():
    global count,frontPtr
    if isEmpty():
        print("Empty")
        return False
    count=count-1
    item=Queue[frontPtr]
    frontPtr=(frontPtr+1)%limit
    return item

def printAll():
    global frontPtr,tailPtr
    for i in range(frontPtr,(tailPtr+1)%limit):
        print(Queue[i],end=" ")

""" testing """
if __name__ == '__main__':

    for i in range(8):
        enQueue( i )
        print("     %d enQueue "%i)
        printAll()
        print()

    for i in range(3):
        print("     %d deQueue"% deQueue())
        printAll()
        print()

    for i in range(9,13):
        enQueue( i )
        print("     %d enQueue "%i)
        printAll()
        print()

