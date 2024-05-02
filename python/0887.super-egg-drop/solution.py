# Created by asetti2002 at 2024/04/25 19:36
# leetgo: 1.4.3
# https://leetcode.com/problems/super-egg-drop/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        m = 0
        while dp[m][k] < n:
            m += 1
            for i in range(1, k + 1):
                dp[m][i] = dp[m - 1][i - 1] + dp[m - 1][i] + 1
        return m
# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().superEggDrop(k, n)
    print("\noutput:", serialize(ans, "integer"))
