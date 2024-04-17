# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-finish-the-race/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tires: List[List[int]] = deserialize("List[List[int]]", read_line())
    changeTime: int = deserialize("int", read_line())
    numLaps: int = deserialize("int", read_line())
    ans = Solution().minimumFinishTime(tires, changeTime, numLaps)
    print("\noutput:", serialize(ans, "integer"))
