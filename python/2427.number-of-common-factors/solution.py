# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-common-factors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().commonFactors(a, b)
    print("\noutput:", serialize(ans, "integer"))
