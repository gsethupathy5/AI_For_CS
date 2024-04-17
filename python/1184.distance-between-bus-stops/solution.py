# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/distance-between-bus-stops/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    distance: List[int] = deserialize("List[int]", read_line())
    start: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().distanceBetweenBusStops(distance, start, destination)
    print("\noutput:", serialize(ans, "integer"))
