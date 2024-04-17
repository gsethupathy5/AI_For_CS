# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    colors: str = deserialize("str", read_line())
    neededTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(colors, neededTime)
    print("\noutput:", serialize(ans, "integer"))
