# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/is-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isSubsequence(s, t)
    print("\noutput:", serialize(ans, "boolean"))
