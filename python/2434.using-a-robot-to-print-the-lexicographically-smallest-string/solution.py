# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def robotWithString(self, s: str) -> str:
        t = ""
        i, j = 0, len(s) - 1
        
        while i <= j:
            if s[i] < s[j]:
                t += s[i]
                i += 1
            else:
                t += s[j]
                j -= 1
                
        return t
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().robotWithString(s)
    print("\noutput:", serialize(ans, "string"))
