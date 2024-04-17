# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    numsDivide: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums, numsDivide)
    print("\noutput:", serialize(ans, "integer"))
