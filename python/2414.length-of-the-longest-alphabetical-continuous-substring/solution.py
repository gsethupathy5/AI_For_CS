# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        current_len = 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                current_len += 1
            else:
                current_len = 1
                
            max_len = max(max_len, current_len)
        
        return max_len
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestContinuousSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
