def LinearSearch(name,SearchName):
    i=0
    while i<10 and name[i]!=SearchName:
        i=i+1
    if i>=10:
        return-1
    else:
        return i

print(LinearSearch(['j','n','f','a','w','s','c','b','q','p'],"w"))




def BubbleSort(num):
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                tem=num[j+1]
                num[j+1]=num[j]
                num[j]=tem
    return num


def BubbleSort(num):
    swap=True
    while swap==True:
        swap=False
        for j in range(len(num)-i):
            if num[j]>num[j+1]:
                tem=num[j+1]
                num[j+1]=num[j]
                num[j]=tem
        i+=1
    return num


def InsertionSort(num):
    for i in range(1,len(num)):
        InsertV=num[i]
        j=i-1
        while InsertV<num[j] and j>=0:
            num[j+1]=num[j]
            j=j-1
        num[j+1]=InsertV
    return num

print(InsertionSort([2,4,1,67,4,2,1,4,9]))