# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/destroying-asteroids/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    mass: int = deserialize("int", read_line())
    asteroids: List[int] = deserialize("List[int]", read_line())
    ans = Solution().asteroidsDestroyed(mass, asteroids)
    print("\noutput:", serialize(ans, "boolean"))
