# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/find-common-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import collections
        res = collections.Counter(words[0])
        for word in words[1:]:
            res &= collections.Counter(word)
        return list(res.elements())
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().commonChars(words)
    print("\noutput:", serialize(ans, "string[]"))
