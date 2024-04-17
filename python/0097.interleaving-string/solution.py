# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/interleaving-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    s3: str = deserialize("str", read_line())
    ans = Solution().isInterleave(s1, s2, s3)
    print("\noutput:", serialize(ans, "boolean"))
