# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().tilingRectangle(n, m)
    print("\noutput:", serialize(ans, "integer"))
