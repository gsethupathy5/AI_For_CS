# Created by asetti2002 at 2024/04/25 20:23
# leetgo: 1.4.3
# https://leetcode.com/problems/selling-pieces-of-wood/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[[0]*102 for _ in range(102)] for _ in range(102)]
        dp[0][0][0] = 0

        for i, j, k in prices:
            for ii in range(m+1):
                for jj in range(n+1):
                    dp[i][ii][jj] = max(dp[i][ii][jj], dp[k][ii-i][jj-j]+1)
                    dp[k][ii][jj] = max(dp[k][ii][jj], dp[i][ii-j][jj-i]+1)
        return dp[m][n][m]
# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    prices: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sellingWood(m, n, prices)
    print("\noutput:", serialize(ans, "long"))
