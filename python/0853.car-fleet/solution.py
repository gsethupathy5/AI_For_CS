# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/car-fleet/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    position: List[int] = deserialize("List[int]", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().carFleet(target, position, speed)
    print("\noutput:", serialize(ans, "integer"))
