# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countRectangles(rectangles, points)
    print("\noutput:", serialize(ans, "integer[]"))
