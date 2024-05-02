# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = total = 0
        for i, flip in enumerate(flips, 1):
            count += 1 if flip <= count else 0
            total += count == i
        return total
# @lc code=end

if __name__ == "__main__":
    flips: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numTimesAllBlue(flips)
    print("\noutput:", serialize(ans, "integer"))
