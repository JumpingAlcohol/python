def LinearSearch(nums,SearchNum):
    i=0
    while i<len(nums) and nums[i]!=SearchNum:
        i+=1
    if i>=len(nums):
        return -1
    else:
        return i


def BinarySearch(nums,SearchNum):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if SearchNum==nums[mid]:
            return mid
        elif SearchNum>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1


def BinarySearch_recur(nums,SearchNum,low,high):
    if low>high:
        return -1
    else:
        mid=(low+high)//2
        if SearchNum==nums[mid]:
            return mid
        elif SearchNum>nums[mid]:
            return BinarySearch_recur(nums,SearchNum,mid+1,high)
        else:
            return BinarySearch_recur(nums,SearchNum,low,mid-1)


def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                tem=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=tem
    return nums

def bubbleImproved(nums):
    flag=True
    i=0
    while flag==True:
        flag=False
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                tem=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=tem
                flag=True
        i+=1
    return nums

def insertionSort(nums):
    for i in range(1,len(nums)):
        j=i-1
        InsertV=nums[i]
        while j>=0 and InsertV<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=InsertV
    return nums





import random

if __name__=="__main__":
    print("-"*20," LinearSearch ","-"*20)
    nums = [random.randint(1,20) for i in range(10)]
    SearchNum= random.randint(1,20)
    print(nums)
    print(SearchNum)
    print(LinearSearch(nums,SearchNum))


if __name__ =="__main__":
    print("-"*20," BinarySearch ","-"*20)
    nums = [random.randint(1,20) for i in range(10)]
    nums.sort()
    SearchNum = random.randint(1,20)
    print(nums)
    print(SearchNum)
    print(BinarySearch(nums,SearchNum))

    print("-"*20," BinarySearch_recur ","-"*20)
    nums = [random.randint(1,20) for i in range(10)]
    nums.sort()
    SearchNum = random.randint(1,20)
    low = 0
    high = len(nums)-1
    print(nums)
    print(SearchNum)
    print(low)
    print(high)
    print(BinarySearch_recur(nums,SearchNum,low,high))


if __name__ =="__main__":
    print("-"*20," Bubble Sort ","-"*20)
    nums = [random.randint(1,100) for i in range(10)]
    print(nums)
    print(bubbleSort(nums))

    print("-" * 20, " Bubble Sort improved", "-" * 20)
    nums = [random.randint(1, 100) for i in range(10)]
    print(nums)
    print(bubbleImproved(nums))


if __name__ =="__main__":
    print("-"*20," Insertion Sort ","-"*20)
    nums = [random.randint(1,100) for i in range(10)]
    print(nums)
    print(insertionSort(nums))