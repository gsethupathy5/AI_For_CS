# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/push-dominoes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pass
# @lc code=end

if __name__ == "__main__":
    dominoes: str = deserialize("str", read_line())
    ans = Solution().pushDominoes(dominoes)
    print("\noutput:", serialize(ans, "string"))
