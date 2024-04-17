# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    forbidden: List[int] = deserialize("List[int]", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minimumJumps(forbidden, a, b, x)
    print("\noutput:", serialize(ans, "integer"))
