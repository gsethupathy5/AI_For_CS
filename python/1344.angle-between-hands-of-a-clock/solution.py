# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/angle-between-hands-of-a-clock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    hour: int = deserialize("int", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().angleClock(hour, minutes)
    print("\noutput:", serialize(ans, "double"))
