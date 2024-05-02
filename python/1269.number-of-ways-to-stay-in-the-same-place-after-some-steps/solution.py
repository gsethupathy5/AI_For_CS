# Created by asetti2002 at 2024/04/25 20:25
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(arrLen - 1, steps)
        dp = [[0] * (max_pos + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(0, max_pos + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                if j < max_pos:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD

        return dp[steps][0]
# @lc code=end

if __name__ == "__main__":
    steps: int = deserialize("int", read_line())
    arrLen: int = deserialize("int", read_line())
    ans = Solution().numWays(steps, arrLen)
    print("\noutput:", serialize(ans, "integer"))
