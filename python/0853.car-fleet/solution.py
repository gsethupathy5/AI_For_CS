# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/car-fleet/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - pos) / spd for pos, spd in cars]
        fleet_count = 0
        curr_time = 0

        for time in times[::-1]:
            if time > curr_time:
                fleet_count += 1
                curr_time = time

        return fleet_count
# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    position: List[int] = deserialize("List[int]", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().carFleet(target, position, speed)
    print("\noutput:", serialize(ans, "integer"))
