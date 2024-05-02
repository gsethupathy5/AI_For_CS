# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * (maxValue + 1)
        for _ in range(1, n):
            new_dp = [0] * (maxValue + 1)
            for i in range(1, maxValue + 1):
                for j in range(i, maxValue + 1, i):
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    maxValue: int = deserialize("int", read_line())
    ans = Solution().idealArrays(n, maxValue)
    print("\noutput:", serialize(ans, "integer"))
