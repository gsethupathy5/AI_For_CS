# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    h: int = deserialize("int", read_line())
    w: int = deserialize("int", read_line())
    horizontalCuts: List[int] = deserialize("List[int]", read_line())
    verticalCuts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(h, w, horizontalCuts, verticalCuts)
    print("\noutput:", serialize(ans, "integer"))
