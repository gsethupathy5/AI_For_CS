# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-collisions-on-a-road/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countCollisions(self, directions: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    directions: str = deserialize("str", read_line())
    ans = Solution().countCollisions(directions)
    print("\noutput:", serialize(ans, "integer"))
