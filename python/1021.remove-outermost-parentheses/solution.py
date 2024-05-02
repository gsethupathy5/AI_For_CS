# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-outermost-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0
        
        for char in s:
            if char == '(':
                if opened > 0:
                    result.append(char)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    result.append(char)
        
        return "".join(result)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeOuterParentheses(s)
    print("\noutput:", serialize(ans, "string"))
