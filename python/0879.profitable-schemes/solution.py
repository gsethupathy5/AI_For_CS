# Created by asetti2002 at 2024/04/25 19:34
# leetgo: 1.4.3
# https://leetcode.com/problems/profitable-schemes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for members, earn in zip(group, profit):
            for i in range(n, -1, -1):
                for j in range(minProfit, -1, -1):
                    if i + members <= n:
                        dp[i + members][min(minProfit, j + earn)] += dp[i][j]
                        dp[i + members][min(minProfit, j + earn)] %= mod
        return sum(dp[i][-1] for i in range(1, n + 1)) % mod
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    minProfit: int = deserialize("int", read_line())
    group: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().profitableSchemes(n, minProfit, group, profit)
    print("\noutput:", serialize(ans, "integer"))
