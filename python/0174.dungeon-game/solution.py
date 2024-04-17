# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/dungeon-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    dungeon: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().calculateMinimumHP(dungeon)
    print("\noutput:", serialize(ans, "integer"))
