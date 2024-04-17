# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    index: int = deserialize("int", read_line())
    maxSum: int = deserialize("int", read_line())
    ans = Solution().maxValue(n, index, maxSum)
    print("\noutput:", serialize(ans, "integer"))
