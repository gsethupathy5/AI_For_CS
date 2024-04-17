# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/pizza-with-3n-slices/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    slices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSizeSlices(slices)
    print("\noutput:", serialize(ans, "integer"))
