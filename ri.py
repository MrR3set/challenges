# https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    ans = int(str(x)[::-1]) if x>0 else  0-int(str(abs(x))[::-1])
    if ( ( ans - 2147483647 > 0 ) or ( ans + 2147483648 < 0) ):
        return 0
    else:
        return ans



