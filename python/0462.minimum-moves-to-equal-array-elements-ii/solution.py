# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMoves2(nums)
    print("\noutput:", serialize(ans, "integer"))
