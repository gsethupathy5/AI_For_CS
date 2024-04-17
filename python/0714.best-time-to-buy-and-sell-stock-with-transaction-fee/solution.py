# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    fee: int = deserialize("int", read_line())
    ans = Solution().maxProfit(prices, fee)
    print("\noutput:", serialize(ans, "integer"))
