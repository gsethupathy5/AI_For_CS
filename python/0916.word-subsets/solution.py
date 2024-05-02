# Created by asetti2002 at 2024/04/25 19:39
# leetgo: 1.4.3
# https://leetcode.com/problems/word-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        res = []
        count = Counter()
        for word in words2:
            count |= Counter(word)
            
        for word in words1:
            if all(word.count(letter) >= count[letter] for letter in count):
                res.append(word)
        
        return res
# @lc code=end

if __name__ == "__main__":
    words1: List[str] = deserialize("List[str]", read_line())
    words2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordSubsets(words1, words2)
    print("\noutput:", serialize(ans, "string[]"))
