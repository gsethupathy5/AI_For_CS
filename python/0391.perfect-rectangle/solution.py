# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/perfect-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isRectangleCover(rectangles)
    print("\noutput:", serialize(ans, "boolean"))