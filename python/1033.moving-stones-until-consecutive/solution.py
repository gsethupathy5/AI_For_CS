# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/moving-stones-until-consecutive/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().numMovesStones(a, b, c)
    print("\noutput:", serialize(ans, "integer[]"))
