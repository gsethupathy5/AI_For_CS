# Created by asetti2002 at 2024/04/25 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/watering-plants/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        water = capacity

        for i in range(n):
            if plants[i] > water:
                steps += 2 * (i + 1)
                water = capacity
            water -= plants[i]
        
        return steps + n + 1
# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().wateringPlants(plants, capacity)
    print("\noutput:", serialize(ans, "integer"))
