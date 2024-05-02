# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-distinct-roll-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 6 for _ in range(n)]

        for j in range(6):
            dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(6):
                for k in range(6):
                    if math.gcd(j + 1, k + 1) == 1 and abs(j - k) > 1:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        
        return sum(dp[-1]) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().distinctSequences(n)
    print("\noutput:", serialize(ans, "integer"))
