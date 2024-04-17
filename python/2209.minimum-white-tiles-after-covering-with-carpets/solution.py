# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    floor: str = deserialize("str", read_line())
    numCarpets: int = deserialize("int", read_line())
    carpetLen: int = deserialize("int", read_line())
    ans = Solution().minimumWhiteTiles(floor, numCarpets, carpetLen)
    print("\noutput:", serialize(ans, "integer"))
