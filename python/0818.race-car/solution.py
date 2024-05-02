# Created by asetti2002 at 2024/04/25 19:07
# leetgo: 1.4.3
# https://leetcode.com/problems/race-car/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] + [float('inf')] * (target)
        for t in range(1, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2)
            dp[t] = min(dp[t], k + 1 + dp[2 ** k - 1 - t])
        return dp[target]
# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    ans = Solution().racecar(target)
    print("\noutput:", serialize(ans, "integer"))
