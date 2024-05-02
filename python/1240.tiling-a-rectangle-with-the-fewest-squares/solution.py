# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = float('inf')
                for k in range(1, min(i, j)+1):
                    dp[i][j] = min(dp[i][j], 1 + dp[i-k][j] + dp[k][j-k])
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j-k] + dp[i-k][k])
                    
        return dp[n][m]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().tilingRectangle(n, m)
    print("\noutput:", serialize(ans, "integer"))
