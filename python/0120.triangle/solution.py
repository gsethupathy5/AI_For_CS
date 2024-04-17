# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    triangle: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotal(triangle)
    print("\noutput:", serialize(ans, "integer"))
