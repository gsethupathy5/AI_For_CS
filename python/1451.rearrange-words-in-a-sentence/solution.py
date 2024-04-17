# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/rearrange-words-in-a-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def arrangeWords(self, text: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().arrangeWords(text)
    print("\noutput:", serialize(ans, "string"))
