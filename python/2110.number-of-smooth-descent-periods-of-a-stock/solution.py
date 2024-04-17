# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getDescentPeriods(prices)
    print("\noutput:", serialize(ans, "long"))
