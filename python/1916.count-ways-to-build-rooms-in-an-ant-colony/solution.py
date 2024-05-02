# Created by asetti2002 at 2024/04/25 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    prevRoom: List[int] = deserialize("List[int]", read_line())
    ans = Solution().waysToBuildRooms(prevRoom)
    print("\noutput:", serialize(ans, "integer"))
