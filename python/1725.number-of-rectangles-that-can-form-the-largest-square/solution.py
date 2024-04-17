# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countGoodRectangles(rectangles)
    print("\noutput:", serialize(ans, "integer"))
