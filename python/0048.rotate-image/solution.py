# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/rotate-image/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
