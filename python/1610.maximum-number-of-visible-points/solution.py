# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-visible-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    angle: int = deserialize("int", read_line())
    location: List[int] = deserialize("List[int]", read_line())
    ans = Solution().visiblePoints(points, angle, location)
    print("\noutput:", serialize(ans, "integer"))
