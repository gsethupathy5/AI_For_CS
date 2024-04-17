# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    students: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMovesToSeat(seats, students)
    print("\noutput:", serialize(ans, "integer"))
