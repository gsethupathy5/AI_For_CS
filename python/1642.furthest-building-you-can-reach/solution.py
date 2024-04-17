# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/furthest-building-you-can-reach/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    bricks: int = deserialize("int", read_line())
    ladders: int = deserialize("int", read_line())
    ans = Solution().furthestBuilding(heights, bricks, ladders)
    print("\noutput:", serialize(ans, "integer"))
