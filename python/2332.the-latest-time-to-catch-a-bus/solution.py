# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    buses: List[int] = deserialize("List[int]", read_line())
    passengers: List[int] = deserialize("List[int]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().latestTimeCatchTheBus(buses, passengers, capacity)
    print("\noutput:", serialize(ans, "integer"))
