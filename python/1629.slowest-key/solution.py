# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/slowest-key/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    releaseTimes: List[int] = deserialize("List[int]", read_line())
    keysPressed: str = deserialize("str", read_line())
    ans = Solution().slowestKey(releaseTimes, keysPressed)
    print("\noutput:", serialize(ans, "character"))
