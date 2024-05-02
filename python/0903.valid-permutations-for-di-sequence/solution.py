# Created by asetti2002 at 2024/04/25 19:37
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-permutations-for-di-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(i + 1):
                if s[i - 1] == 'D':
                    for k in range(j, i):
                        dp[i][j] += dp[i - 1][k]
                else:
                    for k in range(j):
                        dp[i][j] += dp[i - 1][k]
                dp[i][j] %= MOD
        
        return sum(dp[n]) % MOD
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numPermsDISequence(s)
    print("\noutput:", serialize(ans, "integer"))
