# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-distance-to-closest-person/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDistToClosest(seats)
    print("\noutput:", serialize(ans, "integer"))
