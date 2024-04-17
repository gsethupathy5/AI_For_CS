# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countValidWords(self, sentence: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().countValidWords(sentence)
    print("\noutput:", serialize(ans, "integer"))
