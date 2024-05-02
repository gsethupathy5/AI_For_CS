# Created by asetti2002 at 2024/04/25 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/prison-cells-after-n-days/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nextDay(cells):
            new_cells = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
            return new_cells
        
        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n
            
            if n > 0:
                n -= 1
                cells = nextDay(cells)
        
        return cells
# @lc code=end

if __name__ == "__main__":
    cells: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().prisonAfterNDays(cells, n)
    print("\noutput:", serialize(ans, "integer[]"))
