# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/24-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    cards: List[int] = deserialize("List[int]", read_line())
    ans = Solution().judgePoint24(cards)
    print("\noutput:", serialize(ans, "boolean"))
