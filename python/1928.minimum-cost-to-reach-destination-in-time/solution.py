# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    maxTime: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    passingFees: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(maxTime, edges, passingFees)
    print("\noutput:", serialize(ans, "integer"))
