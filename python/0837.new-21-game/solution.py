# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/new-21-game/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + maxPts + 1)
        total = 0.0
        
        for i in range(k, min(n, k + maxPts) + 1):
            dp[i] = 1.0
            total += 1.0
        
        for i in range(k - 1, -1, -1):
            dp[i] = total / maxPts
            total = total - dp[i + maxPts] + dp[i]
        
        return dp[0]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    maxPts: int = deserialize("int", read_line())
    ans = Solution().new21Game(n, k, maxPts)
    print("\noutput:", serialize(ans, "double"))
