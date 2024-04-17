# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    maxLetters: int = deserialize("int", read_line())
    minSize: int = deserialize("int", read_line())
    maxSize: int = deserialize("int", read_line())
    ans = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print("\noutput:", serialize(ans, "integer"))
