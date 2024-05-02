# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/keys-and-rooms/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = [0]
        
        while keys:
            key = keys.pop()
            visited.add(key)
            for new_key in rooms[key]:
                if new_key not in visited:
                    keys.append(new_key)
        
        return len(visited) == len(rooms)
# @lc code=end

if __name__ == "__main__":
    rooms: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canVisitAllRooms(rooms)
    print("\noutput:", serialize(ans, "boolean"))
