# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/permutation-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().checkInclusion(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))