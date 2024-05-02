# Created by asetti2002 at 2024/04/25 20:22
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        to_remove = to_remove.union(set(stack))
        
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)
        
        return ''.join(result)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minRemoveToMakeValid(s)
    print("\noutput:", serialize(ans, "string"))
