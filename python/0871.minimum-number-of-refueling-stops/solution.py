# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-refueling-stops/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    startFuel: int = deserialize("int", read_line())
    stations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minRefuelStops(target, startFuel, stations)
    print("\noutput:", serialize(ans, "integer"))
