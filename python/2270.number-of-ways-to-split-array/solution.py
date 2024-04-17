# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-split-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().waysToSplitArray(nums)
    print("\noutput:", serialize(ans, "integer"))
