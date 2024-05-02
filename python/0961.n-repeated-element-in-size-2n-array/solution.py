# Created by asetti2002 at 2024/04/25 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == len(nums)//2:
                return num
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().repeatedNTimes(nums)
    print("\noutput:", serialize(ans, "integer"))
