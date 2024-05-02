# Created by asetti2002 at 2024/04/25 20:29
# leetgo: 1.4.3
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def freqAlphabets(self, s: str) -> str:
        decoded = ""
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                decoded = chr(num + 96) + decoded
                i -= 3
            else:
                num = int(s[i])
                decoded = chr(num + 96) + decoded
                i -= 1
        
        return decoded
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().freqAlphabets(s)
    print("\noutput:", serialize(ans, "string"))
