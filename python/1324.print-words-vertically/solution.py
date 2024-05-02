# Created by asetti2002 at 2024/04/25 20:31
# leetgo: 1.4.3
# https://leetcode.com/problems/print-words-vertically/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        res = [''] * max_len
        
        for i in range(max_len):
            for word in words:
                res[i] += word[i] if i < len(word) else ' '
        
        return [word.rstrip() for word in res]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().printVertically(s)
    print("\noutput:", serialize(ans, "string[]"))
