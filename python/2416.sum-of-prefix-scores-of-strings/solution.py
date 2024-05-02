# Created by asetti2002 at 2024/05/01 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def count_prefixes(word, words):
            count = 0
            for w in words:
                if w.startswith(word):
                    count += 1
            return count
        
        result = []
        for word in words:
            total = 0
            for i in range(1, len(word) + 1):
                total += count_prefixes(word[:i], words)
            result.append(total)
        
        return result
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().sumPrefixScores(words)
    print("\noutput:", serialize(ans, "integer[]"))
