# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(k, prices)
    print("\noutput:", serialize(ans, "integer"))
