# Created by asetti2002 at 2024/04/25 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/constrained-subsequence-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], max(dp[max(0, i-k):i]) + nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().constrainedSubsetSum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
