# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/heaters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    houses: List[int] = deserialize("List[int]", read_line())
    heaters: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findRadius(houses, heaters)
    print("\noutput:", serialize(ans, "integer"))
