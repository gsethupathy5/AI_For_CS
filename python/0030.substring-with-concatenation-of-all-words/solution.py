# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findSubstring(s, words)
    print("\noutput:", serialize(ans, "integer[]"))
