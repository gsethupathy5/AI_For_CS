# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 0:
            return 1
        elif n == 1:
            return 4
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 4
        
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] * 3 + dp[i - 2] * 2) % MOD
        
        return dp[n]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countHousePlacements(n)
    print("\noutput:", serialize(ans, "integer"))
