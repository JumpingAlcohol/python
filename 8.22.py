import random

"""
Test frame of Bubble sort
"""

# double for ascending
def bubbleSort(nums):
    for i in range(len(nums)-1):
       for j in range(len(nums)-i-1):
           if nums[j]>nums[j+1]:
               tem=nums[j+1]
               nums[j+1]=nums[j]
               nums[j]=tem
    return nums
               
                


def bubbleImproved(nums):
    flag=True
    i=0
    while flag==True:
       flag=False
       for j in range(len(nums)-i-1):
           if nums[j]>nums[j+1]:
               tem=nums[j+1]
               nums[j+1]=nums[j]
               nums[j]=tem
               flag=True
    i=i+1
    return nums


if __name__ =="__main__":
    print("-"*20," Bubble Sort ","-"*20)
    nums = [random.randint(1,100) for i in range(10)]
    print(nums)
    bubbleSort(nums)
    print(nums)

    print("-" * 20, " Bubble Sort improved", "-" * 20)
    nums = [random.randint(1, 100) for i in range(10)]
    print(nums)
    bubbleImproved(nums)
    print(nums)


    # test frame of insertion sort
import random
def insertionSort(nums):
    for i in range(1,len(nums)):
        InsertV=nums[i]
        j=i-1
        while InsertV<nums[j] and j>=0:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=InsertV
    return nums



if __name__ =="__main__":
    print("-"*20," Insertion Sort ","-"*20)
    nums = [random.randint(1,100) for i in range(10)]
    print(nums)
    insertionSort(nums)
    print(nums)




#BinarySearch
def BinarySearch(nums,SearchNum):
    low=0
    high=len(nums)-1   
    while low<=high:
        mid=(low+high)//2
        if SearchNum==nums[mid]:
            return mid
        elif SearchNum<nums[mid]:
            high=mid-1
        elif SearchNum>nums[mid]:
            low=mid+1
    return -1

print(BinarySearch([1,2,3,4,5,6,7,8,9],8))


def binarySearch_recur(nums,item,low,high):
    if low > high:
        return -1
    else:
        mid=(low+high)//2
        if item==nums[mid]:
            return mid
        elif item>nums[mid]:
            return binarySearch_recur(nums,item,mid+1,high)
        else:
            return binarySearch_recur(nums,item,low,mid-1)

print(binarySearch_recur([1,2,3,4,5,6,7,8,9],8,1,9))


