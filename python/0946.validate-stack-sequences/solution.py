# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/validate-stack-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    pushed: List[int] = deserialize("List[int]", read_line())
    popped: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validateStackSequences(pushed, popped)
    print("\noutput:", serialize(ans, "boolean"))
