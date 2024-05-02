# Created by asetti2002 at 2024/05/01 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        nums1.sort()
        nums2.sort()
        
        dp = [[float('inf')] * (k2 + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            diff = abs(nums1[i - 1] - nums2[i - 1])
            dp[i][0] = dp[i - 1][0] + diff
            
        for i in range(1, n + 1):
            for j in range(1, min(i, k2) + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + abs(nums1[i - 1] - nums2[i - 1]), dp[i - 1][j])
                    
        return dp[n][k2]
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k1: int = deserialize("int", read_line())
    k2: int = deserialize("int", read_line())
    ans = Solution().minSumSquareDiff(nums1, nums2, k1, k2)
    print("\noutput:", serialize(ans, "long"))
