# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        total_cost = 0
        max_cost = 0
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] != nums[i-1]:
                total_cost += max_cost # add the maximum cost before resetting
                max_cost = 0 # reset
                
            max_cost = max(max_cost, cost[i]) # keep track of the maximum cost
        
        total_cost += max_cost # add the final max cost
        
        return total_cost
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(nums, cost)
    print("\noutput:", serialize(ans, "long"))
