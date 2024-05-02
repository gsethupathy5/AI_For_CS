# Created by asetti2002 at 2024/04/25 19:36
# leetgo: 1.4.3
# https://leetcode.com/problems/fair-candy-swap/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sa, sb = sum(aliceSizes), sum(bobSizes)
        set_b = set(bobSizes)
        for x in aliceSizes:
            if (x + (sb - sa) // 2) in set_b:
                return [x, x + (sb - sa) // 2]
# @lc code=end

if __name__ == "__main__":
    aliceSizes: List[int] = deserialize("List[int]", read_line())
    bobSizes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fairCandySwap(aliceSizes, bobSizes)
    print("\noutput:", serialize(ans, "integer[]"))
