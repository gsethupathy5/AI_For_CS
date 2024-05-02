# Created by asetti2002 at 2024/05/01 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-operations-to-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        nums.sort(key=lambda x: x == 0)
        return nums
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().applyOperations(nums)
    print("\noutput:", serialize(ans, "integer[]"))
