# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/rings-and-rods/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPoints(self, rings: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rings: str = deserialize("str", read_line())
    ans = Solution().countPoints(rings)
    print("\noutput:", serialize(ans, "integer"))
