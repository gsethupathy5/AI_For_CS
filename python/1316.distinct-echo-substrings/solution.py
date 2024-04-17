# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/distinct-echo-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().distinctEchoSubstrings(text)
    print("\noutput:", serialize(ans, "integer"))
