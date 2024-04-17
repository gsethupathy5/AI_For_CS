# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/car-fleet-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        

# @lc code=end

if __name__ == "__main__":
    cars: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getCollisionTimes(cars)
    print("\noutput:", serialize(ans, "double[]"))
