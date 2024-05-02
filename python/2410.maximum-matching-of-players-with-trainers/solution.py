# Created by asetti2002 at 2024/05/01 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player_index = 0
        trainer_index = 0
        count = 0
        
        while player_index < len(players) and trainer_index < len(trainers):
            if players[player_index] <= trainers[trainer_index]:
                count += 1
                player_index += 1
                trainer_index += 1
            else:
                trainer_index += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    players: List[int] = deserialize("List[int]", read_line())
    trainers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().matchPlayersAndTrainers(players, trainers)
    print("\noutput:", serialize(ans, "integer"))
