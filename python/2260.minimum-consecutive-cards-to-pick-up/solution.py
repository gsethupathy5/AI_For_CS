# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    cards: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCardPickup(cards)
    print("\noutput:", serialize(ans, "integer"))
