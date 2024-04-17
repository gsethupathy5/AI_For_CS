# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/4sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().fourSum(nums, target)
    print("\noutput:", serialize(ans, "integer[][]"))
