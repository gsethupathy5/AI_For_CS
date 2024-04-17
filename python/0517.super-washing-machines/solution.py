# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/super-washing-machines/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    machines: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMinMoves(machines)
    print("\noutput:", serialize(ans, "integer"))
