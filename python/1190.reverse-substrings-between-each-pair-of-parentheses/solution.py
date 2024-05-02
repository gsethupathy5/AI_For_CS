# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur_str = ''
        
        for char in s:
            if char == ')':
                tmp = ''
                while stack[-1] != '(':
                    tmp += stack.pop()
                
                stack.pop()
                stack += list(tmp)
            
            else:
                stack.append(char)
        
        return ''.join(stack)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reverseParentheses(s)
    print("\noutput:", serialize(ans, "string"))
