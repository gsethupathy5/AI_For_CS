# Created by asetti2002 at 2024/04/25 20:33
# leetgo: 1.4.3
# https://leetcode.com/problems/jump-game-v/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Add your code here
        pass
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().maxJumps(arr, d)
    print("\noutput:", serialize(ans, "integer"))
