# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().colorTheGrid(m, n)
    print("\noutput:", serialize(ans, "integer"))
