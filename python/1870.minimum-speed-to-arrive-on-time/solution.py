# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        

# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    hour: float = deserialize("float", read_line())
    ans = Solution().minSpeedOnTime(dist, hour)
    print("\noutput:", serialize(ans, "integer"))
