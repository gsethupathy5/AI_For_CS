# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rounds: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostVisited(n, rounds)
    print("\noutput:", serialize(ans, "integer[]"))
