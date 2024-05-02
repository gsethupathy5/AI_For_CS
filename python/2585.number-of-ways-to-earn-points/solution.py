# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for count, mark in types:
            for j in range(target, mark - 1, -1):
                for k in range(1, count + 1):
                    if j - k * mark >= 0:
                        dp[j] = (dp[j] + dp[j - k * mark]) % MOD
        
        return dp[target]
# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    types: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().waysToReachTarget(target, types)
    print("\noutput:", serialize(ans, "integer"))
