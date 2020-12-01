# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    canvas = ['']*numRows
    rowCurr = 0
    direction = -1
    ans = ""

    for letter in s:
        canvas[rowCurr] = canvas[rowCurr]+letter
        if rowCurr >= numRows-1 or rowCurr == 0:
            direction=direction*-1
        rowCurr += direction

    for i in canvas:
        ans = ans + i

    return ans
