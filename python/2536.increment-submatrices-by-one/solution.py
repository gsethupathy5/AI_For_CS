# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/increment-submatrices-by-one/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        for query in queries:
            row1, col1, row2, col2 = query
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    mat[i][j] += 1
        
        return mat
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().rangeAddQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[][]"))
