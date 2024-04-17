# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minSteps(s, t)
    print("\noutput:", serialize(ans, "integer"))
