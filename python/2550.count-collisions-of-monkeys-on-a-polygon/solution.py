# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def monkeyMove(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().monkeyMove(n)
    print("\noutput:", serialize(ans, "integer"))
