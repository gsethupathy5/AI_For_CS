# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/reshape-the-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    r: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().matrixReshape(mat, r, c)
    print("\noutput:", serialize(ans, "integer[][]"))