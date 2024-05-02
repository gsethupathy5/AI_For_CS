# Created by asetti2002 at 2024/04/25 20:23
# leetgo: 1.4.3
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_count = 0
        rows = [0] * m
        cols = [0] * n
        
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 != 0:
                    odd_count += 1
        
        return odd_count
# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    indices: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().oddCells(m, n, indices)
    print("\noutput:", serialize(ans, "integer"))
