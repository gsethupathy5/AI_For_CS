# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/destroy-sequential-targets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    space: int = deserialize("int", read_line())
    ans = Solution().destroyTargets(nums, space)
    print("\noutput:", serialize(ans, "integer"))
