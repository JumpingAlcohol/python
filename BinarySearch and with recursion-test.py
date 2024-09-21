def BinarySearch(nums,item):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if item==nums[mid]:
            return mid
        elif item<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1



def BinarySearch_recur(nums,item,low,high):
    if low>high:
        return -1
    else:
        mid=(low+high)//2
        if item==nums[mid]:
            return mid
        elif item>nums[mid]:
            return BinarySearch_recur(nums,item,mid+1,high)
        else:
            return BinarySearch_recur(nums,item,low,mid-1)
        
import random
if __name__ =="__main__":
    print("-"*20," BinarySearch ","-"*20)
    nums = [random.randint(1,20) for i in range(10)]
    nums.sort()
    item = random.randint(1,20)
    print(nums)
    print(item)
    print(BinarySearch(nums,item))

    print("-"*20," BinarySearch_recur ","-"*20)
    nums = [random.randint(1,20) for i in range(10)]
    nums.sort()
    item = random.randint(1,20)
    low = 0
    high = len(nums)-1
    print(nums)
    print(item)
    print(low)
    print(high)
    print(BinarySearch_recur(nums,item,low,high))

  