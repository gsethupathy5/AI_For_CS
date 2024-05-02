# Created by asetti2002 at 2024/05/01 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-beautiful-partitions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        primes = {'2', '3', '5', '7'}
        
        def is_prime(num):
            return num in primes
        
        n = len(s)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for l in range(min(i, minLength), i + 1):
                    if is_prime(s[l-1]) and not is_prime(s[i-1]):
                        dp[i][j] = (dp[i][j] + dp[l-1][j-1]) % MOD
        
        return dp[n][k]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    minLength: int = deserialize("int", read_line())
    ans = Solution().beautifulPartitions(s, k, minLength)
    print("\noutput:", serialize(ans, "integer"))
