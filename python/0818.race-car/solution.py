# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/race-car/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def racecar(self, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    ans = Solution().racecar(target)
    print("\noutput:", serialize(ans, "integer"))
