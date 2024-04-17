# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(cost)
    print("\noutput:", serialize(ans, "integer"))
