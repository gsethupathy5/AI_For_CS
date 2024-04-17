# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-value-after-insertion/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: str = deserialize("str", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().maxValue(n, x)
    print("\noutput:", serialize(ans, "string"))
