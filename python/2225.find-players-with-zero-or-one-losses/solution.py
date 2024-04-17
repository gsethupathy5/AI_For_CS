# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    matches: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findWinners(matches)
    print("\noutput:", serialize(ans, "integer[][]"))
