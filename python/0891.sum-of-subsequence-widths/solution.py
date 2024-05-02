# Created by asetti2002 at 2024/04/25 19:36
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-subsequence-widths/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7
        
        res = 0
        p = 1
        
        for i in range(n):
            res = (res + (nums[i] - nums[n - 1 - i]) * p) % MOD
            p = (p << 1) % MOD
        
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumSubseqWidths(nums)
    print("\noutput:", serialize(ans, "integer"))
