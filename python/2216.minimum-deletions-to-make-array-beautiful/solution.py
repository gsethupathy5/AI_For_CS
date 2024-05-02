# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        deletion = 0
        for i in range(0, n, 2):
            if i < n - 1:
                if nums[i] == nums[i + 1]:
                    deletion += 1
        return deletion
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDeletion(nums)
    print("\noutput:", serialize(ans, "integer"))
