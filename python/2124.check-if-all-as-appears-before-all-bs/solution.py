# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkString(self, s: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().checkString(s)
    print("\noutput:", serialize(ans, "boolean"))
