# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-trees-with-factors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        arr.sort()
        dp = {}
        
        for i in arr:
            dp[i] = 1
            for j in arr:
                if j > i**0.5:
                    break
                if i % j == 0 and i // j in dp:
                    dp[i] += dp[j] * dp[i//j] if i // j != j else dp[j] * dp[i//j]
                    
        return sum(dp.values()) % MOD
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFactoredBinaryTrees(arr)
    print("\noutput:", serialize(ans, "integer"))
