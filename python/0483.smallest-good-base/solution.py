# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-good-base/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: str = deserialize("str", read_line())
    ans = Solution().smallestGoodBase(n)
    print("\noutput:", serialize(ans, "string"))
