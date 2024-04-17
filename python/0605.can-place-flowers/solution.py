# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/can-place-flowers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    flowerbed: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().canPlaceFlowers(flowerbed, n)
    print("\noutput:", serialize(ans, "boolean"))
