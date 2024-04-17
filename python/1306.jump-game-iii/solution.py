# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/jump-game-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().canReach(arr, start)
    print("\noutput:", serialize(ans, "boolean"))
