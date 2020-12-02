# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rowsDict = dict.fromkeys(range(0,numRows))

    rowCurr = 0
    direction = -1

    for letter in s:
        rowsDict[rowCurr] = rowsDict[rowCurr]+letter if rowsDict[rowCurr] is not None else ''
        if rowCurr >= numRows-1 or rowCurr == 0:
            direction=direction*-1
        rowCurr += direction


    return "".join([v for k,v in rowsDict.items()])