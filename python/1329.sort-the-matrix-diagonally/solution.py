# Created by asetti2002 at 2024/04/25 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-matrix-diagonally/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort_diagonal(i, j):
            diagonal = []
            while i < len(mat) and j < len(mat[0]):
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = diagonal.pop()
        
        for i in range(len(mat)):
            sort_diagonal(i, 0)
        for j in range(1, len(mat[0])):
            sort_diagonal(0, j)
        
        return mat
# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().diagonalSort(mat)
    print("\noutput:", serialize(ans, "integer[][]"))
