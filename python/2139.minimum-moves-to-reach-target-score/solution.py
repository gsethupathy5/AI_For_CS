# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    maxDoubles: int = deserialize("int", read_line())
    ans = Solution().minMoves(target, maxDoubles)
    print("\noutput:", serialize(ans, "integer"))
