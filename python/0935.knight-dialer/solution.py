# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/knight-dialer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * 10

        for _ in range(n - 1):
            new_dp = [0] * 10
            
            new_dp[0] = (dp[4] + dp[6]) % MOD
            new_dp[1] = (dp[6] + dp[8]) % MOD
            new_dp[2] = (dp[7] + dp[9]) % MOD
            new_dp[3] = (dp[4] + dp[8]) % MOD
            new_dp[4] = (dp[3] + dp[9] + dp[0]) % MOD
            new_dp[6] = (dp[1] + dp[7] + dp[0]) % MOD
            new_dp[7] = (dp[2] + dp[6]) % MOD
            new_dp[8] = (dp[1] + dp[3]) % MOD
            new_dp[9] = (dp[2] + dp[4]) % MOD

            dp = new_dp

        return sum(dp) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().knightDialer(n)
    print("\noutput:", serialize(ans, "integer"))
