# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().areNumbersAscending(s)
    print("\noutput:", serialize(ans, "boolean"))
