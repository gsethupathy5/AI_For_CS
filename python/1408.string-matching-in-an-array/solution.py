# Created by asetti2002 at 2024/04/25 20:40
# leetgo: 1.4.3
# https://leetcode.com/problems/string-matching-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    substrings.append(words[i])
                    break
        return substrings
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().stringMatching(words)
    print("\noutput:", serialize(ans, "string[]"))
