# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/koko-eating-bananas/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    h: int = deserialize("int", read_line())
    ans = Solution().minEatingSpeed(piles, h)
    print("\noutput:", serialize(ans, "integer"))
