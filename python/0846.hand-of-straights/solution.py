# Created by asetti2002 at 2024/04/25 19:29
# leetgo: 1.4.3
# https://leetcode.com/problems/hand-of-straights/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort the hand array
        hand.sort()
        
        # Create a Counter dictionary to count the occurrences of each card
        count = Counter(hand)
        
        # Iterate through the sorted hand array
        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
        
        return True
# @lc code=end

if __name__ == "__main__":
    hand: List[int] = deserialize("List[int]", read_line())
    groupSize: int = deserialize("int", read_line())
    ans = Solution().isNStraightHand(hand, groupSize)
    print("\noutput:", serialize(ans, "boolean"))
