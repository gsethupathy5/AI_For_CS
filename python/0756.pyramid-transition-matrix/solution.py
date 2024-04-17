# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/pyramid-transition-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    bottom: str = deserialize("str", read_line())
    allowed: List[str] = deserialize("List[str]", read_line())
    ans = Solution().pyramidTransition(bottom, allowed)
    print("\noutput:", serialize(ans, "boolean"))
