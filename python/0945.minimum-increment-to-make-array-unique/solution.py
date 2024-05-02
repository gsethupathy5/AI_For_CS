# Created by asetti2002 at 2024/04/25 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                moves += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return moves
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrementForUnique(nums)
    print("\noutput:", serialize(ans, "integer"))
