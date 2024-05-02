# Created by asetti2002 at 2024/05/01 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        costs.sort()
        ans = float('inf')
        total = 0
        
        for i in range(k, n+1):
            total += costs[i-1]
            ans = min(ans, total)
            if i < n and i >= candidates:
                total -= costs[i-candidates]
        
        return ans
# @lc code=end

if __name__ == "__main__":
    costs: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    candidates: int = deserialize("int", read_line())
    ans = Solution().totalCost(costs, k, candidates)
    print("\noutput:", serialize(ans, "long"))
