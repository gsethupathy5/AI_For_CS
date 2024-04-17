# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/hand-of-straights/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    hand: List[int] = deserialize("List[int]", read_line())
    groupSize: int = deserialize("int", read_line())
    ans = Solution().isNStraightHand(hand, groupSize)
    print("\noutput:", serialize(ans, "boolean"))
