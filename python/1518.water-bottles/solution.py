# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/water-bottles/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    numBottles: int = deserialize("int", read_line())
    numExchange: int = deserialize("int", read_line())
    ans = Solution().numWaterBottles(numBottles, numExchange)
    print("\noutput:", serialize(ans, "integer"))
