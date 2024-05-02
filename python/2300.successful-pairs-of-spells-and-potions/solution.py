# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        for i in range(len(spells)):
            count = 0
            for potion in potions:
                if spells[i] * potion >= success:
                    count += 1
            pairs.append(count)
        return pairs
# @lc code=end

if __name__ == "__main__":
    spells: List[int] = deserialize("List[int]", read_line())
    potions: List[int] = deserialize("List[int]", read_line())
    success: int = deserialize("int", read_line())
    ans = Solution().successfulPairs(spells, potions, success)
    print("\noutput:", serialize(ans, "integer[]"))
