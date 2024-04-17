# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-vi/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    aliceValues: List[int] = deserialize("List[int]", read_line())
    bobValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVI(aliceValues, bobValues)
    print("\noutput:", serialize(ans, "integer"))
