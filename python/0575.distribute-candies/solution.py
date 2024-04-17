# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-candies/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    candyType: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distributeCandies(candyType)
    print("\noutput:", serialize(ans, "integer"))
