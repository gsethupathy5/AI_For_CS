# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/sentence-similarity-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    sentence1: str = deserialize("str", read_line())
    sentence2: str = deserialize("str", read_line())
    ans = Solution().areSentencesSimilar(sentence1, sentence2)
    print("\noutput:", serialize(ans, "boolean"))
