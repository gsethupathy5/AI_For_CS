# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/last-substring-in-lexicographical-order/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def lastSubstring(self, s: str) -> str:
        # Solution code here
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lastSubstring(s)
    print("\noutput:", serialize(ans, "string"))
