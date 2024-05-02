# Created by asetti2002 at 2024/04/25 19:40
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        
        for char in s:
            if char == '(':
                stack.append('(')
            else:
                if len(stack) == 0:
                    ans += 1
                else:
                    stack.pop()
        
        return len(stack) + ans
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minAddToMakeValid(s)
    print("\noutput:", serialize(ans, "integer"))
