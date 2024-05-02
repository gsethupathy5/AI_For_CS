# Created by asetti2002 at 2024/04/25 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        d = {}
        for domino in dominoes:
            key = tuple(sorted(domino))
            count += d.get(key, 0)
            d[key] = d.get(key, 0) + 1
        return count
# @lc code=end

if __name__ == "__main__":
    dominoes: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numEquivDominoPairs(dominoes)
    print("\noutput:", serialize(ans, "integer"))
