# Created by asetti2002 at 2024/05/01 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * 2001 for _ in range(2001)]
        
        dp[0][startPos] = 1
        
        for i in range(1, k + 1):
            for j in range(-1000, 1001):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
        
        return dp[k][endPos]
# @lc code=end

if __name__ == "__main__":
    startPos: int = deserialize("int", read_line())
    endPos: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfWays(startPos, endPos, k)
    print("\noutput:", serialize(ans, "integer"))
