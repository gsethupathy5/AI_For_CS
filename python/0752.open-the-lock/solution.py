# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/open-the-lock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    deadends: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().openLock(deadends, target)
    print("\noutput:", serialize(ans, "integer"))
