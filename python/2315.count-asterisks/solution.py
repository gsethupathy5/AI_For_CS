# Created by asetti2002 at 2024/05/01 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/count-asterisks/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        i = 0
        
        while i < len(s):
            if s[i] == '|':
                while i < len(s) and s[i] != '|':
                    i += 1
            if i < len(s) and s[i] == '*':
                count += 1
            i += 1
            
        return count
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countAsterisks(s)
    print("\noutput:", serialize(ans, "integer"))
