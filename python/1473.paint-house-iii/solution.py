# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/paint-house-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    houses: List[int] = deserialize("List[int]", read_line())
    cost: List[List[int]] = deserialize("List[List[int]]", read_line())
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minCost(houses, cost, m, n, target)
    print("\noutput:", serialize(ans, "integer"))
