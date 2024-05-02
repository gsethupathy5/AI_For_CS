# Created by asetti2002 at 2024/04/25 19:31
# leetgo: 1.4.3
# https://leetcode.com/problems/score-of-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(2 * last, 1)
        return stack[0]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().scoreOfParentheses(s)
    print("\noutput:", serialize(ans, "integer"))
