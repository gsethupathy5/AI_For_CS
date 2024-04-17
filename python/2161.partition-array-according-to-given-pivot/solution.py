# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    pivot: int = deserialize("int", read_line())
    ans = Solution().pivotArray(nums, pivot)
    print("\noutput:", serialize(ans, "integer[]"))
