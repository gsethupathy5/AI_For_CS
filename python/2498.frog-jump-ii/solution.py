# Created by asetti2002 at 2024/05/01 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/frog-jump-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * n
        dp[1] = stones[1]
        for i in range(2, n):
            for j in range(1, i):
                dp[i] = max(dp[i], min(dp[j] + abs(stones[i] - stones[j]), stones[i] - stones[j]))
        return dp[n - 1]
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxJump(stones)
    print("\noutput:", serialize(ans, "integer"))
