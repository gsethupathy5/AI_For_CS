# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/circular-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        circular = False
        for i in range(len(words)):
            if words[i][-1].lower() == words[(i+1)%len(words)][0].lower():
                circular = True
            else:
                circular = False
                break
        return circular
# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().isCircularSentence(sentence)
    print("\noutput:", serialize(ans, "boolean"))
