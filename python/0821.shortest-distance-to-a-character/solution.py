# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-distance-to-a-character/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    c: str = deserialize("str", read_line())
    ans = Solution().shortestToChar(s, c)
    print("\noutput:", serialize(ans, "integer[]"))
