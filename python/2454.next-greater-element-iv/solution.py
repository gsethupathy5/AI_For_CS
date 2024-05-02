# Created by asetti2002 at 2024/05/01 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/next-greater-element-iv/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                prev_idx = stack.pop()
                if stack:
                    ans[stack[-1]] = max(ans[stack[-1]], nums[i])
                ans[prev_idx] = nums[i]
            stack.append(i)
        return ans
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().secondGreaterElement(nums)
    print("\noutput:", serialize(ans, "integer[]"))
