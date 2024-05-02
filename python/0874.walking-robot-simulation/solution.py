# Created by asetti2002 at 2024/04/25 19:34
# leetgo: 1.4.3
# https://leetcode.com/problems/walking-robot-simulation/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
            obstacles = set(map(tuple, obstacles))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            x = y = idx = ans = 0
            for command in commands:
                if command == -2:
                    idx = (idx - 1) % 4
                elif command == -1:
                    idx = (idx + 1) % 4
                else:
                    dx, dy = directions[idx]
                    for _ in range(command):
                        if (x + dx, y + dy) not in obstacles:
                            x += dx
                            y += dy
                        ans = max(ans, x*x + y*y)
            return ans
# @lc code=end

if __name__ == "__main__":
    commands: List[int] = deserialize("List[int]", read_line())
    obstacles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().robotSim(commands, obstacles)
    print("\noutput:", serialize(ans, "integer"))
