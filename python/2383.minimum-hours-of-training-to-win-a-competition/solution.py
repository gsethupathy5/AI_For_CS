# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        def can_win(curr_energy, curr_experience, energy_needed, experience_needed):
            return curr_energy > energy_needed and curr_experience > experience_needed
        
        n = len(energy)
        min_hours = 0
        
        for i in range(n):
            needed_energy = energy[i]
            needed_experience = experience[i]
            
            while not can_win(initialEnergy, initialExperience, needed_energy, needed_experience):
                if initialEnergy >= initialExperience:
                    initialEnergy += 1
                else:
                    initialExperience += 1
                min_hours += 1
            
            initialEnergy -= needed_energy
            initialExperience += needed_experience
        
        return min_hours
# @lc code=end

if __name__ == "__main__":
    initialEnergy: int = deserialize("int", read_line())
    initialExperience: int = deserialize("int", read_line())
    energy: List[int] = deserialize("List[int]", read_line())
    experience: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    print("\noutput:", serialize(ans, "integer"))
