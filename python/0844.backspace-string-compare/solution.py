# Created by asetti2002 at 2024/04/25 19:29
# leetgo: 1.4.3
# https://leetcode.com/problems/backspace-string-compare/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        return backspace(s) == backspace(t)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().backspaceCompare(s, t)
    print("\noutput:", serialize(ans, "boolean"))
