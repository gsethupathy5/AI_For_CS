# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-repair-cars/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    ranks: List[int] = deserialize("List[int]", read_line())
    cars: int = deserialize("int", read_line())
    ans = Solution().repairCars(ranks, cars)
    print("\noutput:", serialize(ans, "long"))
