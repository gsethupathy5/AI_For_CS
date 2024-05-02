# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for t in range(j, target + 1):
                    dp[i][t] = (dp[i][t] + dp[i - 1][t - j]) % mod
        return dp[n][target]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numRollsToTarget(n, k, target)
    print("\noutput:", serialize(ans, "integer"))
