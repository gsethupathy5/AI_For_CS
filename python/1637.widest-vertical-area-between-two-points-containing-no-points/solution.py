# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxWidthOfVerticalArea(points)
    print("\noutput:", serialize(ans, "integer"))
