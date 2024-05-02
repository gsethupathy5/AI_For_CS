# Created by asetti2002 at 2024/04/25 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/distinct-echo-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        res = set()
        
        for i in range(n):
            for j in range(i+1, n):
                if j-i <= n-j and text[i:j] == text[j:j+i]:
                    res.add(text[i:j])
        
        return len(res)
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().distinctEchoSubstrings(text)
    print("\noutput:", serialize(ans, "integer"))
