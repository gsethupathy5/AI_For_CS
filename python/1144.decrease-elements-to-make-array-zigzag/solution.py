# Created by asetti2002 at 2024/04/25 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        odd_sum = even_sum = 0
        for i in range(len(nums)):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < len(nums) - 1 else float('inf')
            odd_sum += max(0, nums[i] - min(left, right) + 1) if i % 2 == 0 else 0
            even_sum += max(0, nums[i] - min(left, right) + 1) if i % 2 != 0 else 0
        return min(odd_sum, even_sum)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().movesToMakeZigzag(nums)
    print("\noutput:", serialize(ans, "integer"))
