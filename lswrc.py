
# https://leetcode.com/problems/longest-substring-without-repeating-characters/



# Inefficient


def lengthOfLongestSubstring(s: str) -> int:
    # Convert str -> arr
    arr = list(s)
    # Declare variables
    subStrMax = 0
    # Loop trough all elements
    for cIndex in range(0,len(arr)):
        # Loop trough remaining elements
        subStrCurr = 0
        visited = {}
        for rIndex in range(cIndex,len(arr)):
            # Check visited = TRUE
            if arr[rIndex] in visited:
                break
            # Else 
            else:
                # Add 1 to subStrCurr
                visited[arr[rIndex]]=1
                subStrCurr+=1
        # get max(subStrMax, subStrCurr)
        if subStrCurr>subStrMax:
            print("New max", subStrCurr, ' prev was ', subStrMax)
            subStrMax = subStrCurr
            print("Max", subStrMax)




    
lengthOfLongestSubstring("qqwweerrttyyuuiioopp")