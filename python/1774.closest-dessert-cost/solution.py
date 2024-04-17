# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/closest-dessert-cost/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    baseCosts: List[int] = deserialize("List[int]", read_line())
    toppingCosts: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().closestCost(baseCosts, toppingCosts, target)
    print("\noutput:", serialize(ans, "integer"))
