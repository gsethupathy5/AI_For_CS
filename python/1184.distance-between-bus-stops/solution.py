# Created by asetti2002 at 2024/04/25 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/distance-between-bus-stops/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = sum(distance)
        clockwise_distance = sum(distance[min(start, destination):max(start, destination)])
        return min(clockwise_distance, total_distance - clockwise_distance)
# @lc code=end

if __name__ == "__main__":
    distance: List[int] = deserialize("List[int]", read_line())
    start: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().distanceBetweenBusStops(distance, start, destination)
    print("\noutput:", serialize(ans, "integer"))
