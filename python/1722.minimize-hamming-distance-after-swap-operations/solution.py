# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    source: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    allowedSwaps: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumHammingDistance(source, target, allowedSwaps)
    print("\noutput:", serialize(ans, "integer"))
