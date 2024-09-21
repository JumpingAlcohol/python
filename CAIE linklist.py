#Question 1(a):
class node():
    def __init__(self,data=-1,nextNode=-1):
        #define a node record
        #param data:STRING
        #param point:INTEGER
        self.data=data
        self.nextNode=nextNode
MAX=10



#Question 1(c) (i):
def outputNodes(linkedList,startPointer):
    cur=startPointer
    while cur !=-1:
        print(linkedList[cur].data,end=" ")
        cur=linkedList[cur].nextNode
    print()


#Question 1(d)(i):
def addNode(linkedList,startPointer,emptyList)->tuple[int,int,bool]:
    if emptyList==-1:
        success=False
    else:
        newNode=emptyList
        emptyList=linkedList[emptyList].nextNode

        item=int(input("Enter"))
        linkedList[newNode].data=item
        linkedList[newNode].nextNode=-1
        #insert at tail
        pre=-1
        cur=startPointer
        while cur!=-1:
            pre=cur
            cur=linkedList[cur].nextNode
        if pre==-1:#insert to an empty list
            startPointer=newNode
        else:
            linkedList[pre].nextNode=newNode
            success=True
    return startPointer,emptyList,success

#Question 1(e)(i):
def deleteNode(linkedList,startPointer,emptyList)->tuple[int,int,bool]:
    #user input data to be deleted
    item=int(input("Enter"))
    #find the data in the list
    pre=-1
    cur=startPointer
    while cur!=-1 and linkedList[cur].data!=item:
        pre=cur
        cur=linkedList[cur].nextNode
    if cur==-1:
        success=False
        return startPointer,emptyList,success
    else:#take the node 
        if pre==-1:#delete head node
            cur=startPointer
            startPointer=linkedList[startPointer].nextNode
        else:#delete node in the middle/tail
            linkedList[pre].nextNode=linkedList[cur].nextNode
    #return the node to the free list
        linkedList[cur].nextNode=emptyList
        emptyList=cur
        success=True
        return startPointer,emptyList,success

if __name__=="__main__":
    #Question 1(b):
    #DECLARE linkedList:ARRAY[0:9] OF node
    linkedList=[node("") for i in range(MAX)]

    linkedList[0]=node(1,1)
    linkedList[1]=node(5,4)
    linkedList[2]=node(6,7)
    linkedList[3]=node(7,-1)
    linkedList[4]=node(2,2)
    linkedList[5]=node(0,6)
    linkedList[6]=node(0,8)
    linkedList[7]=node(56,3)
    linkedList[8]=node(0,9)
    linkedList[9]=node(0,-1)

    startPointer=0
    emptyList=5

    #Question 1(c) (ii):
    outputNodes(linkedList,startPointer)

    #Question 1(d)(ii):
    outputNodes(linkedList,startPointer)
    startPointer,emptyList,success=addNode(linkedList,startPointer,emptyList)
    outputNodes(linkedList,startPointer)

    #Question 1(e)(ii):
    for i in range(2):
        startPointer,emptyList,success=deleteNode(linkedList,startPointer,emptyList)
        if success:
            print("Delete successfully")
        else:
            print("Failed to delete")