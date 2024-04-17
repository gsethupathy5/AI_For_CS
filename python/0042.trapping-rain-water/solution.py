# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))
