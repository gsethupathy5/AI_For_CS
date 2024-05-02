# Created by asetti2002 at 2024/04/25 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/queens-that-can-attack-the-king/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        def is_valid(x, y):
            return 0 <= x < 8 and 0 <= y < 8
        
        for dx, dy in directions:
            x, y = king
            while is_valid(x, y):
                if [x, y] in queens:
                    result.append([x, y])
                    break
                x += dx
                y += dy
        
        return result
# @lc code=end

if __name__ == "__main__":
    queens: List[List[int]] = deserialize("List[List[int]]", read_line())
    king: List[int] = deserialize("List[int]", read_line())
    ans = Solution().queensAttacktheKing(queens, king)
    print("\noutput:", serialize(ans, "integer[][]"))
