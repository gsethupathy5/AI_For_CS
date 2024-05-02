# Created by asetti2002 at 2024/04/25 19:06
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-sum-of-averages/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        
        total_sum = [0.0]
        for num in nums:
            total_sum.append(total_sum[-1] + num)
        
        for i in range(1, n + 1):
            dp[i][1] = total_sum[i] / i
        
        for i in range(1, n + 1):
            for j in range(2, k + 1):
                for p in range(j-1, i):
                    dp[i][j] = max(dp[i][j], dp[p][j-1] + (total_sum[i] - total_sum[p]) / (i - p))
        
        return dp[n][k]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().largestSumOfAverages(nums, k)
    print("\noutput:", serialize(ans, "double"))
