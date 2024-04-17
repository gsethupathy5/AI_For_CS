# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    players: List[int] = deserialize("List[int]", read_line())
    trainers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().matchPlayersAndTrainers(players, trainers)
    print("\noutput:", serialize(ans, "integer"))
