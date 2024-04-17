# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/reaching-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    sx: int = deserialize("int", read_line())
    sy: int = deserialize("int", read_line())
    tx: int = deserialize("int", read_line())
    ty: int = deserialize("int", read_line())
    ans = Solution().reachingPoints(sx, sy, tx, ty)
    print("\noutput:", serialize(ans, "boolean"))
