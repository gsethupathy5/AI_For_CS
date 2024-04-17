# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-square-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    c: int = deserialize("int", read_line())
    ans = Solution().judgeSquareSum(c)
    print("\noutput:", serialize(ans, "boolean"))
