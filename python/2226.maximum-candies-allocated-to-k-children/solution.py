# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    candies: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumCandies(candies, k)
    print("\noutput:", serialize(ans, "integer"))
