# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    firstPlayer: int = deserialize("int", read_line())
    secondPlayer: int = deserialize("int", read_line())
    ans = Solution().earliestAndLatest(n, firstPlayer, secondPlayer)
    print("\noutput:", serialize(ans, "integer[]"))
