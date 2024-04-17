# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    balls: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getProbability(balls)
    print("\noutput:", serialize(ans, "double"))
