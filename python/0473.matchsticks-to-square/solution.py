# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/matchsticks-to-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    matchsticks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makesquare(matchsticks)
    print("\noutput:", serialize(ans, "boolean"))
