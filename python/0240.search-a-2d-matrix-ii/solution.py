# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
