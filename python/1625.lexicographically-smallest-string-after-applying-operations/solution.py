# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().findLexSmallestString(s, a, b)
    print("\noutput:", serialize(ans, "string"))
