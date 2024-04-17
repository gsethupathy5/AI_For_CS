# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/cinema-seat-allocation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    reservedSeats: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxNumberOfFamilies(n, reservedSeats)
    print("\noutput:", serialize(ans, "integer"))
