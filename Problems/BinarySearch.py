def binarysearch(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

index = binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 11)
print(index)