# Created by asetti2002 at 2024/04/25 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/two-city-scheduling/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total_cost = 0
        n = len(costs) // 2
        
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]
            
        return total_cost
# @lc code=end

if __name__ == "__main__":
    costs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().twoCitySchedCost(costs)
    print("\noutput:", serialize(ans, "integer"))
