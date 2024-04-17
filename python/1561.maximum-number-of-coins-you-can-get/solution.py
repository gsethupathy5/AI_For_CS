# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCoins(piles)
    print("\noutput:", serialize(ans, "integer"))
