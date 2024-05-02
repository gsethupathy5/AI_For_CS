# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/pizza-with-3n-slices/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        return max(self.helper(slices[1:-1], n), self.helper(slices[:-1], n))
    
    def helper(self, slices, n):
        dp = [[0] * (n + 1) for _ in range(len(slices) + 1)]
        
        for i in range(1, len(slices) + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i-1][j], (dp[i-2][j-1] if i > 1 else 0) + slices[i-1])

        return dp[-1][-1]
# @lc code=end

if __name__ == "__main__":
    slices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSizeSlices(slices)
    print("\noutput:", serialize(ans, "integer"))
