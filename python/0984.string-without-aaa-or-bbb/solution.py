# Created by asetti2002 at 2024/04/25 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/string-without-aaa-or-bbb/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        while a > 0 and b > 0:
            if a > b:
                s += "aab"
                a -= 2
                b -= 1
            elif a < b:
                s += "bba"
                a -= 1
                b -= 2
            else:
                s += "ab"
                a -= 1
                b -= 1
        
        if a > 0:
            s = "a" * a + s
        elif b > 0:
            s = "b" * b + s
        
        return s
# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().strWithout3a3b(a, b)
    print("\noutput:", serialize(ans, "string"))
