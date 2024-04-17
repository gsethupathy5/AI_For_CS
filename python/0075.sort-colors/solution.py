# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-colors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    sortColors(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
