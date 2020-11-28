# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(nums1, nums2) -> float:
    combined = nums1+nums2
    combined.sort()
    if len(combined)==0:
        return 0
    if len(combined)%2 == 0:
        return (combined[int(len(combined)/2)] + combined[int(len(combined)/2)-1])/2
    else:
        return combined[int(len(combined)/2)]




print(findMedianSortedArrays([1,2],[3,4]))