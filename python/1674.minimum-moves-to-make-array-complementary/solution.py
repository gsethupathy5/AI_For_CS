# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().minMoves(nums, limit)
    print("\noutput:", serialize(ans, "integer"))
