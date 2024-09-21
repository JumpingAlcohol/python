# singly linked list

#define a class Node, which include two fields, data  is string , point is integer
class Node():
    def __init__(self,data='',point=-1):       #Constructor
        #define a node record
        #param data:STRING
        #param point:INTEGER
        self.data=data                      #attribute property data
        self.point=point
MAX=10


""" define array named LList which is an array of Node, includes 10 nodes """

LList = [Node("") for i in range(MAX)]


""" initialize free list,   the head pointer of freelist is freeHead"""

for i in range(MAX-1):                      #LList=[Node("",i+1) for i in range(9)]
    LList[i].point=i+1
LList[-1].point=-1      #set inversely. LList[MAX-1].point=-1

freehead=0

""" initialize an empty using list, the head pointer of the using list is startPoint """
startPoint = -1             #head


""" add a node at head """
def addAtHead(item):
    global freehead, startPoint
    if freehead==-1:
       print("The memory is full")
    else:
        #take a node from the free list
        newnode=freehead
        freehead=LList[freehead].point
        #assign value to the new node
        LList[newnode].data=item
        #add at head
        LList[newnode].point=startPoint
        startPoint=newnode

""" add a node at tail"""
def addAtTail(item):
    global freehead, startPoint
    if freehead==-1:
        print("The memory is full")
    else:
        newnode=freehead
        freehead=LList[freehead].point
        LList[newnode].data=item
        LList[newnode].point=-1
        #insert to the tail
        current=startPoint
        previous=-1
        while current!=-1:
            previous=current
            current=LList[current].point
        #insert tail node at head
        if previous==-1:
            startPoint=newnode
        #insert tail node at tail
        else:
            LList[previous].point=newnode
            
    
""" search in list , if find item return location , else return False"""
def searchList(item):
    current=startPoint
    while current!=-1:
        if LList[current].data==item:
            return current
        current=LList[current].point
    return False

""" delete a node from the head and return the item. Empty list return None"""
def delFromHead():
    global freehead, startPoint
    if startPoint==-1:
        return None
    else:
        #delete from the user list
        current=startPoint
        startPoint=LList[current].point
        #put into the free list
        LList[current].point=freehead
        freehead=current
        #return value
        return LList[current].data

""" delete a node from the tail and return the item. Empty list return None"""
def delFromTail():
    global freehead, startPoint
    if startPoint==-1:
        return None
    else:
        current=startPoint
        previous=-1
        while LList[current].point!=-1:
            previous=current
            current=LList[current].point
        if previous==-1:        #delete the only one node
            startPoint=-1
        else:       #delete tail node
            LList[previous].point=-1
        #return to the free list
        LList[current].point=freehead
        freehead=current
        return LList[current].data

""" delete the item node from list, if item is not in the list,return False , else return True"""
def deleteItem(startPoint, item):  # discuss the parameter startPoint
    global freehead
    if startPoint==-1:
        return None
    else:
        current=startPoint
        next=LList[current].point
        if LList[current].data==item:
            startPoint=next
        else:
            while next!=-1 and LList[next].data!=item:
                current=next
                next=LList[next].point
            if next==-1:
                return False
            else:
                LList[current].point=LList[next].point
                LList[next].point=freehead
                freehead=next
                return True
    return startPoint

""" print all items in the list """
def printAll(startPoint):
    current=startPoint
    while current!=-1:
        print(LList[current].data, end=" ")
        current=LList[current].point
    print()



""" main """
if __name__ == "__main__":
    listValue = ["Lucy", "Peter", "Daniel"]

    #insert t at head
    for value in listValue:
        addAtHead(value)
    printAll(startPoint)


    #insert at tail

    listValue = ["Candy","Fergal","Amy"]
    for value in listValue:
        addAtTail(value)
    printAll(startPoint)

    """ 
    let user input a name, and search in the using list 
    and return the index location of the name in the using list
    index begins from 1
    """
    name = input("Please input search name = ")
    st_point=int(input("Please input the start point = "))
    find = searchList(name)

    # according the return value , print out proper message to user.

    if find==False:
        print(name,"can't be found")
    else:
        print(name,"can be found at ",find)

    # if the name is in the using list, then delete it from the list
    deleteItem(st_point,name)
    printAll(startPoint)
    #delete the first one in the using list
    delFromHead()
    printAll(startPoint)
    #delete the last one in the using list
    delFromTail()
    printAll(startPoint)

    #design your own test code to check



    # when you delete an empty list it will deal with it properly



    # when add new item but there isn't memory it will deal with it properly

