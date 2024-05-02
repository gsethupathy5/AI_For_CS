# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-maximum-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i] > 0:
                diff = min(nums[i], nums[i-1])
                nums[i] -= diff
                nums[i-1] += diff
        return max(nums)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizeArrayValue(nums)
    print("\noutput:", serialize(ans, "integer"))
