# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/detect-capital/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().detectCapitalUse(word)
    print("\noutput:", serialize(ans, "boolean"))
