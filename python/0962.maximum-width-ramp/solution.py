# Created by asetti2002 at 2024/04/25 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-width-ramp/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxWidthRamp(nums)
    print("\noutput:", serialize(ans, "integer"))
