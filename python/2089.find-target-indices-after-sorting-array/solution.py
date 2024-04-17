# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().targetIndices(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
