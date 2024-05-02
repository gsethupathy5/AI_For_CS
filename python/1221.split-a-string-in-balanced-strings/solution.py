# Created by asetti2002 at 2024/04/25 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        result = 0
        
        for char in s:
            if char == 'R':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                result += 1
        
        return result
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().balancedStringSplit(s)
    print("\noutput:", serialize(ans, "integer"))
