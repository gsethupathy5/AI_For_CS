# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/queens-that-can-attack-the-king/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    queens: List[List[int]] = deserialize("List[List[int]]", read_line())
    king: List[int] = deserialize("List[int]", read_line())
    ans = Solution().queensAttacktheKing(queens, king)
    print("\noutput:", serialize(ans, "integer[][]"))
