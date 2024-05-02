# Created by asetti2002 at 2024/04/25 19:36
# leetgo: 1.4.3
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def count(word):
            res = [0] * 52
            for i, c in enumerate(word):
                res[ord(c) - ord('a') + 26 * (i % 2)] += 1
            return tuple(res)
        
        return len({count(word) for word in words})
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSpecialEquivGroups(words)
    print("\noutput:", serialize(ans, "integer"))
