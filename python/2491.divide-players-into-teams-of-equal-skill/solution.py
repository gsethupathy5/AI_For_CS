# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    skill: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dividePlayers(skill)
    print("\noutput:", serialize(ans, "long"))
