# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-boomerang/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[1][1] - points[2][1]) != (points[1][0] - points[2][0]) * (points[0][1] - points[1][1])
# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isBoomerang(points)
    print("\noutput:", serialize(ans, "boolean"))
