# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/rearranging-fruits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    basket1: List[int] = deserialize("List[int]", read_line())
    basket2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(basket1, basket2)
    print("\noutput:", serialize(ans, "long"))
