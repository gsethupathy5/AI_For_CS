# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/text-justification/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    maxWidth: int = deserialize("int", read_line())
    ans = Solution().fullJustify(words, maxWidth)
    print("\noutput:", serialize(ans, "string[]"))
