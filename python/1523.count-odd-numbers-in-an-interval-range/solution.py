# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().countOdds(low, high)
    print("\noutput:", serialize(ans, "integer"))
