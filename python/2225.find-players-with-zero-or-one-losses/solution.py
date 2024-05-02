# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        for winner, loser in matches:
            if winner not in winners:
                winners[winner] = 0
            if loser not in winners:
                winners[loser] = 0
                
            winners[winner] += 1
            
            if winners[loser] > 0:
                del winners[loser]
        
        return [sorted([player for player, losses in winners.items() if losses == 0]), sorted([player for player, losses in winners.items() if losses == 1])]
# @lc code=end

if __name__ == "__main__":
    matches: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findWinners(matches)
    print("\noutput:", serialize(ans, "integer[][]"))
