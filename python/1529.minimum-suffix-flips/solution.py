# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-suffix-flips/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minFlips(self, target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: str = deserialize("str", read_line())
    ans = Solution().minFlips(target)
    print("\noutput:", serialize(ans, "integer"))
