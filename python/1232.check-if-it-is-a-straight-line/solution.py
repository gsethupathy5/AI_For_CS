# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    coordinates: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkStraightLine(coordinates)
    print("\noutput:", serialize(ans, "boolean"))
