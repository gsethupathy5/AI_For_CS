# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/parsing-a-boolean-expression/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()  # pop the '('
                operator = stack.pop()
                if operator == '&':
                    stack.append(all(seen))
                elif operator == '|':
                    stack.append(any(seen))
                elif operator == '!':
                    stack.append(not seen.pop())
            elif char in "&|!":
                stack.append(char)
            elif char.isalpha():
                stack.append(char == 't')
        return stack[-1]
# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    ans = Solution().parseBoolExpr(expression)
    print("\noutput:", serialize(ans, "boolean"))
