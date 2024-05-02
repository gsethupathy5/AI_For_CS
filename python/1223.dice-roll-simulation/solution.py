# Created by asetti2002 at 2024/04/25 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/dice-roll-simulation/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n)]
        
        for i in range(6):
            dp[0][i][1] = 1
        
        for i in range(1, n):
            for j in range(6):
                for k in range(1, 16):
                    for l in range(6):
                        if l == j:
                            if k < rollMax[l]:
                                dp[i][j][k+1] += dp[i-1][l][k] % MOD
                        else:
                            dp[i][j][1] += dp[i-1][l][k] % MOD
        
        return sum(sum(dp[n-1][j]) for j in range(6)) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rollMax: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dieSimulator(n, rollMax)
    print("\noutput:", serialize(ans, "integer"))
