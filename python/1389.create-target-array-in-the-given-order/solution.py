# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    index: List[int] = deserialize("List[int]", read_line())
    ans = Solution().createTargetArray(nums, index)
    print("\noutput:", serialize(ans, "integer[]"))
