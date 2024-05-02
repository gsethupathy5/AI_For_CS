# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        import itertools
        total_sum = sum(skill)
        if total_sum % len(skill) != 0:
            return -1
        target_sum = total_sum // (len(skill) // 2)
        teams = itertools.combinations(skill, len(skill) // 2)
        chemistry_sum = 0
        for team in teams:
            if sum(team) == target_sum:
                chemistry_sum += team[0] * team[1]
        return chemistry_sum
# @lc code=end

if __name__ == "__main__":
    skill: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dividePlayers(skill)
    print("\noutput:", serialize(ans, "long"))
