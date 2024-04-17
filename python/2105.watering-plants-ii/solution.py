# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/watering-plants-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacityA: int = deserialize("int", read_line())
    capacityB: int = deserialize("int", read_line())
    ans = Solution().minimumRefill(plants, capacityA, capacityB)
    print("\noutput:", serialize(ans, "integer"))
