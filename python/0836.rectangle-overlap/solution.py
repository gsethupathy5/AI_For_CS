# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/rectangle-overlap/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])     # top
# @lc code=end

if __name__ == "__main__":
    rec1: List[int] = deserialize("List[int]", read_line())
    rec2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isRectangleOverlap(rec1, rec2)
    print("\noutput:", serialize(ans, "boolean"))
