# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/rank-teams-by-votes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    votes: List[str] = deserialize("List[str]", read_line())
    ans = Solution().rankTeams(votes)
    print("\noutput:", serialize(ans, "string"))
