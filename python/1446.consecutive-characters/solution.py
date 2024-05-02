# Created by asetti2002 at 2024/04/25 20:42
# leetgo: 1.4.3
# https://leetcode.com/problems/consecutive-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxPower(self, s: str) -> int:
        res = cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        return max(res, cur)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxPower(s)
    print("\noutput:", serialize(ans, "integer"))
