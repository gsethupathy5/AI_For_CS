# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/poor-pigs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    buckets: int = deserialize("int", read_line())
    minutesToDie: int = deserialize("int", read_line())
    minutesToTest: int = deserialize("int", read_line())
    ans = Solution().poorPigs(buckets, minutesToDie, minutesToTest)
    print("\noutput:", serialize(ans, "integer"))
