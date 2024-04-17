# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
