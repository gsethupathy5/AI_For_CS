# Created by asetti2002 at 2024/04/25 19:39
# leetgo: 1.4.3
# https://leetcode.com/problems/reverse-only-letters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        res = []
        for c in s:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        return "".join(res)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reverseOnlyLetters(s)
    print("\noutput:", serialize(ans, "string"))
