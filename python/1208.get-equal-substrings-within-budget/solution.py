# Created by asetti2002 at 2024/04/25 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/get-equal-substrings-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = start = 0
        for end in range(len(s)):
            maxCost -= abs(ord(s[end]) - ord(t[end]))
            if maxCost < 0:
                maxCost += abs(ord(s[start]) - ord(t[start]))
                start += 1
            res = max(res, end - start + 1)
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    maxCost: int = deserialize("int", read_line())
    ans = Solution().equalSubstring(s, t, maxCost)
    print("\noutput:", serialize(ans, "integer"))
