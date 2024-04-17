# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    speed: int = deserialize("int", read_line())
    hoursBefore: int = deserialize("int", read_line())
    ans = Solution().minSkips(dist, speed, hoursBefore)
    print("\noutput:", serialize(ans, "integer"))
