# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-great-partitions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [[[0]*(k+1) for _ in range(k+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for x in range(k+1):
                for y in range(k+1):
                    if i == 0:
                        if x <= y:
                            dp[i][x][y] = 1
                    else:
                        if nums[i-1] >= x:
                            dp[i][x][y] = (dp[i-1][nums[i-1]][y] + dp[i-1][x][y]) % mod
                        else:
                            dp[i][x][y] = dp[i-1][x][y]
        
        total = 0
        for x in range(1, k+1):
            for y in range(x, k+1):
                total = (total + dp[n][x][y]) % mod
        
        return total
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countPartitions(nums, k)
    print("\noutput:", serialize(ans, "integer"))
