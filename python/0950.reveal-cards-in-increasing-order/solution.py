# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    deck: List[int] = deserialize("List[int]", read_line())
    ans = Solution().deckRevealedIncreasing(deck)
    print("\noutput:", serialize(ans, "integer[]"))
