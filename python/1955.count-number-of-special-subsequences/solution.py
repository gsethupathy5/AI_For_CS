# Created by asetti2002 at 2024/04/25 19:02
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-special-subsequences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [0, 0, 0]
        for num in nums:
            dp[num] = (2*dp[num] + (num == 0)) % MOD
        return dp[2] % MOD
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countSpecialSubsequences(nums)
    print("\noutput:", serialize(ans, "integer"))
