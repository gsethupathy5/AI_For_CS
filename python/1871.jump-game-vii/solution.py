# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/jump-game-vii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    minJump: int = deserialize("int", read_line())
    maxJump: int = deserialize("int", read_line())
    ans = Solution().canReach(s, minJump, maxJump)
    print("\noutput:", serialize(ans, "boolean"))
