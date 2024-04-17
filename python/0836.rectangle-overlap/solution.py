# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/rectangle-overlap/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    rec1: List[int] = deserialize("List[int]", read_line())
    rec2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isRectangleOverlap(rec1, rec2)
    print("\noutput:", serialize(ans, "boolean"))
