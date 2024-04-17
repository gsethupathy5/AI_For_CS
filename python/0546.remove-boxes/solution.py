# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    boxes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeBoxes(boxes)
    print("\noutput:", serialize(ans, "integer"))
