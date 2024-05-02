# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-arithmetic-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2
        return max(dp.values())
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestArithSeqLength(nums)
    print("\noutput:", serialize(ans, "integer"))
