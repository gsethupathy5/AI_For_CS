# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    baseStr: str = deserialize("str", read_line())
    ans = Solution().smallestEquivalentString(s1, s2, baseStr)
    print("\noutput:", serialize(ans, "string"))
