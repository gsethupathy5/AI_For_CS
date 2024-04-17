# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/repeated-string-match/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    ans = Solution().repeatedStringMatch(a, b)
    print("\noutput:", serialize(ans, "integer"))
