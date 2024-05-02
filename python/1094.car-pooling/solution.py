# Created by asetti2002 at 2024/04/25 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/car-pooling/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        passengers = [0] * 1001
        
        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]
        
        for passenger in passengers:
            capacity -= passenger
            if capacity < 0:
                return False
        
        return True
# @lc code=end

if __name__ == "__main__":
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().carPooling(trips, capacity)
    print("\noutput:", serialize(ans, "boolean"))
