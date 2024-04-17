# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-increasing-quadruplets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countQuadruplets(nums)
    print("\noutput:", serialize(ans, "long"))
