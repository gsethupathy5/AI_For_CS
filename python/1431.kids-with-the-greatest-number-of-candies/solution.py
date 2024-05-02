# Created by asetti2002 at 2024/04/25 20:40
# leetgo: 1.4.3
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
# @lc code=end

if __name__ == "__main__":
    candies: List[int] = deserialize("List[int]", read_line())
    extraCandies: int = deserialize("int", read_line())
    ans = Solution().kidsWithCandies(candies, extraCandies)
    print("\noutput:", serialize(ans, "boolean[]"))
