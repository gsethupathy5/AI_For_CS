# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-it-is-a-good-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isGoodArray(nums)
    print("\noutput:", serialize(ans, "boolean"))
