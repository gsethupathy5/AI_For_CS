# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/fair-candy-swap/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    aliceSizes: List[int] = deserialize("List[int]", read_line())
    bobSizes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fairCandySwap(aliceSizes, bobSizes)
    print("\noutput:", serialize(ans, "integer[]"))
