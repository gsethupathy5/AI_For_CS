# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        for j in range(1, m + 1):
            dp[1][j][1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for kk in range(1, k + 1):
                    dp[i][j][kk] += j * dp[i - 1][j][kk]
                    dp[i][j][kk] %= MOD
                    
                    for jj in range(1, j):
                        dp[i][j][kk] += dp[i - 1][jj][kk - 1]
                        dp[i][j][kk] %= MOD
        
        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numOfArrays(n, m, k)
    print("\noutput:", serialize(ans, "integer"))
