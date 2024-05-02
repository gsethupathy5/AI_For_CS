# Created by asetti2002 at 2024/04/25 19:06
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-triangle-area/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        pass
# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestTriangleArea(points)
    print("\noutput:", serialize(ans, "double"))
