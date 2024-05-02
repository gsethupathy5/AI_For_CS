# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return min(i + 1 for i in range(n) if nums[i] > n - i - 1)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScore(nums)
    print("\noutput:", serialize(ans, "integer"))
