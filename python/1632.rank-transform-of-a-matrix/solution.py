# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/rank-transform-of-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixRankTransform(matrix)
    print("\noutput:", serialize(ans, "integer[][]"))
