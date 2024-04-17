# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-good-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    evil: str = deserialize("str", read_line())
    ans = Solution().findGoodStrings(n, s1, s2, evil)
    print("\noutput:", serialize(ans, "integer"))
