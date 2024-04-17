# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    colors: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDistance(colors)
    print("\noutput:", serialize(ans, "integer"))
