# Created by asetti2002 at 2024/04/25 19:39
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxLeft = nums[0]
        partitionIdx = 0
        curMax = maxLeft
        
        for i in range(1, len(nums)):
            if nums[i] < maxLeft:
                maxLeft = curMax
                partitionIdx = i
            else:
                curMax = max(curMax, nums[i])
        
        return partitionIdx + 1
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().partitionDisjoint(nums)
    print("\noutput:", serialize(ans, "integer"))
