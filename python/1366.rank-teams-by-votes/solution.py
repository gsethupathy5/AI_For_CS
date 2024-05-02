# Created by asetti2002 at 2024/04/25 20:35
# leetgo: 1.4.3
# https://leetcode.com/problems/rank-teams-by-votes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        from collections import defaultdict
        
        counts = defaultdict(lambda: [0]*26)
        for vote in votes:
            for i, team in enumerate(vote):
                counts[team][i] -= 1
        
        sorted_teams = sorted(votes[0], key=lambda x: (counts[x], x))
        return ''.join(sorted_teams)
# @lc code=end

if __name__ == "__main__":
    votes: List[str] = deserialize("List[str]", read_line())
    ans = Solution().rankTeams(votes)
    print("\noutput:", serialize(ans, "string"))
