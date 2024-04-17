# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-happy-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().longestDiverseString(a, b, c)
    print("\noutput:", serialize(ans, "string"))
