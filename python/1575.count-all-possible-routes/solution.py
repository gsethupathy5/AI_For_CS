# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-all-possible-routes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    locations: List[int] = deserialize("List[int]", read_line())
    start: int = deserialize("int", read_line())
    finish: int = deserialize("int", read_line())
    fuel: int = deserialize("int", read_line())
    ans = Solution().countRoutes(locations, start, finish, fuel)
    print("\noutput:", serialize(ans, "integer"))
