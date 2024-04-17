# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/dice-roll-simulation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rollMax: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dieSimulator(n, rollMax)
    print("\noutput:", serialize(ans, "integer"))
