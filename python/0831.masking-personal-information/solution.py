# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/masking-personal-information/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maskPII(self, s: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maskPII(s)
    print("\noutput:", serialize(ans, "string"))
