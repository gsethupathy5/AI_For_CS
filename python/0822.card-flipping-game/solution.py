# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/card-flipping-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    fronts: List[int] = deserialize("List[int]", read_line())
    backs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().flipgame(fronts, backs)
    print("\noutput:", serialize(ans, "integer"))
