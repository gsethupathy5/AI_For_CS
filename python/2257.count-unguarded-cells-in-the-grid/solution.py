# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    guards: List[List[int]] = deserialize("List[List[int]]", read_line())
    walls: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countUnguarded(m, n, guards, walls)
    print("\noutput:", serialize(ans, "integer"))
