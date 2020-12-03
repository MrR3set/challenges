def searchInsert(nums, target):
    left, right = 0, len(nums)-1
    while (left<=right):
        mid= int((left + right)/2)
        midValue = nums[mid]
        if midValue < target:
            left = mid+1        
        elif midValue > target:
            right = mid-1
        elif midValue == target:
            return mid
    return left


print('solution',searchInsert([124,1000,2048484],300))