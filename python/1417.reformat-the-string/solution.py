# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/reformat-the-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reformat(self, s: str) -> str:
        import random
        letters = []
        digits = []
        
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                digits.append(char)
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        res = ''
        
        if len(letters) < len(digits):
            letters, digits = digits, letters
        
        while letters and digits:
            res += letters.pop()
            res += digits.pop()
        
        if letters:
            res += letters.pop()
        
        if digits:
            res = digits.pop() + res
        
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reformat(s)
    print("\noutput:", serialize(ans, "string"))
