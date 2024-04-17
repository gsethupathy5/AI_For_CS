# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/swap-adjacent-in-lr-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    start: str = deserialize("str", read_line())
    end: str = deserialize("str", read_line())
    ans = Solution().canTransform(start, end)
    print("\noutput:", serialize(ans, "boolean"))
