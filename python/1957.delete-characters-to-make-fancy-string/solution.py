# Created by asetti2002 at 2024/04/25 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) >= 2 and char == stack[-1] == stack[-2]:
                continue
            stack.append(char)
        return ''.join(stack)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().makeFancyString(s)
    print("\noutput:", serialize(ans, "string"))
