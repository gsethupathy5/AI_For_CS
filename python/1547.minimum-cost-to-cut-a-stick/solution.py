# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    cuts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(n, cuts)
    print("\noutput:", serialize(ans, "integer"))
