# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startWords: List[str] = deserialize("List[str]", read_line())
    targetWords: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordCount(startWords, targetWords)
    print("\noutput:", serialize(ans, "integer"))
