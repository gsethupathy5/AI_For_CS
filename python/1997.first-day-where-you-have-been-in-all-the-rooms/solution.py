# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nextVisit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstDayBeenInAllRooms(nextVisit)
    print("\noutput:", serialize(ans, "integer"))
