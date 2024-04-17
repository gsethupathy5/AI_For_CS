# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/detonate-the-maximum-bombs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    bombs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumDetonation(bombs)
    print("\noutput:", serialize(ans, "integer"))
