# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/n-th-tribonacci-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().tribonacci(n)
    print("\noutput:", serialize(ans, "integer"))
