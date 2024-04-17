# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/goal-parser-interpretation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def interpret(self, command: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    command: str = deserialize("str", read_line())
    ans = Solution().interpret(command)
    print("\noutput:", serialize(ans, "string"))
