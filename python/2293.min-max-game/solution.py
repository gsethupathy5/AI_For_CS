# Created by asetti2002 at 2024/05/01 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/min-max-game/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for i in range(0, len(nums) // 2):
                newNums.append(min(nums[2*i], nums[2*i+1]))
                newNums.append(max(nums[2*i], nums[2*i+1]))
            nums = newNums
        return nums[0]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMaxGame(nums)
    print("\noutput:", serialize(ans, "integer"))
