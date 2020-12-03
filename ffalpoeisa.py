# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):

    left, right = 0,len(nums)-1
    ans = [-1,-1]

    while left<=right:
        mid = int((left + right)/2)
        midValue = nums[mid]

        if midValue>target:
            right = mid-1
        elif midValue<target:
            left = mid+1
        elif midValue == target:
            left = right = mid
            while left>=0 and nums[left] == target:
                left -=1
            while right <= len(nums)-1 and nums[right] == target:
                right+=1
            return [left+1,right-1]

    return ans






print("sol", searchRange([5,5,5,5,5,7],5))