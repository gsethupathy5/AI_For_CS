# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/water-and-jug-problem/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().canMeasureWater(x, y, target)
    print("\noutput:", serialize(ans, "boolean"))
