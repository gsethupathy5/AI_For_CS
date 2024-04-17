# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    pieces: List[str] = deserialize("List[str]", read_line())
    positions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countCombinations(pieces, positions)
    print("\noutput:", serialize(ans, "integer"))
