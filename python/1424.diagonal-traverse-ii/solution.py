# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/diagonal-traverse-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findDiagonalOrder(nums)
    print("\noutput:", serialize(ans, "integer[]"))
