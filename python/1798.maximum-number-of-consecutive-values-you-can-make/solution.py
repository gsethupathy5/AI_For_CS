# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getMaximumConsecutive(coins)
    print("\noutput:", serialize(ans, "integer"))
