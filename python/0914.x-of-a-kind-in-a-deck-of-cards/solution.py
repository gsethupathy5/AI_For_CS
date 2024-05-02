# Created by asetti2002 at 2024/04/25 19:39
# leetgo: 1.4.3
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        pass
# @lc code=end

if __name__ == "__main__":
    deck: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hasGroupsSizeX(deck)
    print("\noutput:", serialize(ans, "boolean"))
