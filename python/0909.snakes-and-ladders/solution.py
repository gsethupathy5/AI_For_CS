# Created by asetti2002 at 2024/04/25 19:38
# leetgo: 1.4.3
# https://leetcode.com/problems/snakes-and-ladders/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().snakesAndLadders(board)
    print("\noutput:", serialize(ans, "integer"))
