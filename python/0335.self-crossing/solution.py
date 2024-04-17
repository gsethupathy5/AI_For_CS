# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/self-crossing/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    distance: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isSelfCrossing(distance)
    print("\noutput:", serialize(ans, "boolean"))
