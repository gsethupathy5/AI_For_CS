# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    start: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().canChange(start, target)
    print("\noutput:", serialize(ans, "boolean"))
