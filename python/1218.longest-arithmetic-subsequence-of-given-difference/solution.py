# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
        return max(dp.values())
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    difference: int = deserialize("int", read_line())
    ans = Solution().longestSubsequence(arr, difference)
    print("\noutput:", serialize(ans, "integer"))
