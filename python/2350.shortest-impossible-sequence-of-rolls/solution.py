# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rolls: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().shortestSequence(rolls, k)
    print("\noutput:", serialize(ans, "integer"))
