# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/maximal-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalRectangle(matrix)
    print("\noutput:", serialize(ans, "integer"))