# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/k-similar-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().kSimilarity(s1, s2)
    print("\noutput:", serialize(ans, "integer"))
