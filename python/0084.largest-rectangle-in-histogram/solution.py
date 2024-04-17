# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestRectangleArea(heights)
    print("\noutput:", serialize(ans, "integer"))
