# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/restore-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - 1 - len(str(k)), -1), -1):
                if s[j] == '0':
                    continue
                num = int(s[j:i])
                if 1 <= num <= k:
                    dp[i] = (dp[i] + dp[j]) % mod
                    
        return dp[n]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfArrays(s, k)
    print("\noutput:", serialize(ans, "integer"))
