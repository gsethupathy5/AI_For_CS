# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().finalPrices(prices)
    print("\noutput:", serialize(ans, "integer[]"))
