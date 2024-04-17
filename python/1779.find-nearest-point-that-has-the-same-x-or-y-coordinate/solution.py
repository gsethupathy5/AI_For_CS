# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().nearestValidPoint(x, y, points)
    print("\noutput:", serialize(ans, "integer"))
