# Created by asetti2002 at 2024/05/01 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/time-to-cross-a-bridge/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    time: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findCrossingTime(n, k, time)
    print("\noutput:", serialize(ans, "integer"))
