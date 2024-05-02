# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n
        dp[0] = 1
        
        for day in range(1, n):
            dp[day] = dp[day - 1] + (dp[day - delay] if day >= delay else 0) - (dp[day - forget - 1] if day > forget else 0)
            dp[day] %= MOD
        
        return dp[n - 1]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    delay: int = deserialize("int", read_line())
    forget: int = deserialize("int", read_line())
    ans = Solution().peopleAwareOfSecret(n, delay, forget)
    print("\noutput:", serialize(ans, "integer"))
