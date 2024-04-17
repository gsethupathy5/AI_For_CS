# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfWays(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfWays(s)
    print("\noutput:", serialize(ans, "long"))
