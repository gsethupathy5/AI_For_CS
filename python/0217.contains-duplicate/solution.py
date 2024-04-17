# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/contains-duplicate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().containsDuplicate(nums)
    print("\noutput:", serialize(ans, "boolean"))
