# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-teams/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rating: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numTeams(rating)
    print("\noutput:", serialize(ans, "integer"))
