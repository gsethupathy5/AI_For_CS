# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-paths-with-max-score/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        pass
# @lc code=end

if __name__ == "__main__":
    board: List[str] = deserialize("List[str]", read_line())
    ans = Solution().pathsWithMaxScore(board)
    print("\noutput:", serialize(ans, "integer[]"))
