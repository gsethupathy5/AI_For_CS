# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/car-pooling/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().carPooling(trips, capacity)
    print("\noutput:", serialize(ans, "boolean"))
