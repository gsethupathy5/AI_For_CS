# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/new-21-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    maxPts: int = deserialize("int", read_line())
    ans = Solution().new21Game(n, k, maxPts)
    print("\noutput:", serialize(ans, "double"))
