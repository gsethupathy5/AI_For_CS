# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    seats: int = deserialize("int", read_line())
    ans = Solution().minimumFuelCost(roads, seats)
    print("\noutput:", serialize(ans, "long"))
