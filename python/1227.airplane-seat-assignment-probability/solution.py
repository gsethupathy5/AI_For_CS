# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/airplane-seat-assignment-probability/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().nthPersonGetsNthSeat(n)
    print("\noutput:", serialize(ans, "double"))
