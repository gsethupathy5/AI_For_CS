# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/reverse-prefix-of-word/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ch: str = deserialize("str", read_line())
    ans = Solution().reversePrefix(word, ch)
    print("\noutput:", serialize(ans, "string"))
