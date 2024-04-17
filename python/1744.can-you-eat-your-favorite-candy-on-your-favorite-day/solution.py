# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    candiesCount: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canEat(candiesCount, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
