# Created by asetti2002 at 2024/04/25 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/rank-transform-of-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        import numpy as np
        m, n = len(matrix), len(matrix[0])
        mat = np.array(matrix)
        
        flattened = [(i, j) for i in range(m) for j in range(n)]
        flattened.sort(key=lambda x: mat[x[0], x[1]])
        
        ranks = [[0 for _ in range(n)] for _ in range(m)]
        col_ranks = [0] * n
        row_ranks = [0] * m
        
        for i, (row, col) in enumerate(flattened):
            if i == 0 or mat[row][col] != mat[flattened[i - 1][0]][flattened[i - 1][1]]:
                rank = max(row_ranks[row], col_ranks[col]) + 1
            else:
                rank = ranks[flattened[i - 1][0]][flattened[i - 1][1]]
                
            ranks[row][col] = rank
            row_ranks[row] = rank
            col_ranks[col] = rank
        
        return ranks
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixRankTransform(matrix)
    print("\noutput:", serialize(ans, "integer[][]"))
