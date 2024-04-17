# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-repeating-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    quantity: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canDistribute(nums, quantity)
    print("\noutput:", serialize(ans, "boolean"))
