# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/two-city-scheduling/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    costs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().twoCitySchedCost(costs)
    print("\noutput:", serialize(ans, "integer"))