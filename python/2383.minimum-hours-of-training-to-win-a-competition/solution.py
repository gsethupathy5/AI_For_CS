# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    initialEnergy: int = deserialize("int", read_line())
    initialExperience: int = deserialize("int", read_line())
    energy: List[int] = deserialize("List[int]", read_line())
    experience: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    print("\noutput:", serialize(ans, "integer"))
