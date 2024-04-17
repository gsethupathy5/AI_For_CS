# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/circular-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().isCircularSentence(sentence)
    print("\noutput:", serialize(ans, "boolean"))
