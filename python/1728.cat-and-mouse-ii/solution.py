# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/cat-and-mouse-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[str] = deserialize("List[str]", read_line())
    catJump: int = deserialize("int", read_line())
    mouseJump: int = deserialize("int", read_line())
    ans = Solution().canMouseWin(grid, catJump, mouseJump)
    print("\noutput:", serialize(ans, "boolean"))
