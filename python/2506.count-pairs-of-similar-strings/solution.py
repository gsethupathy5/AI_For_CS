# Created by asetti2002 at 2024/05/01 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/count-pairs-of-similar-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pair_count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    pair_count += 1
        return pair_count
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().similarPairs(words)
    print("\noutput:", serialize(ans, "integer"))
