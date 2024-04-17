# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/count-days-spent-together/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arriveAlice: str = deserialize("str", read_line())
    leaveAlice: str = deserialize("str", read_line())
    arriveBob: str = deserialize("str", read_line())
    leaveBob: str = deserialize("str", read_line())
    ans = Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print("\noutput:", serialize(ans, "integer"))
