# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/132-pattern/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().find132pattern(nums)
    print("\noutput:", serialize(ans, "boolean"))
