# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/meeting-rooms-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    meetings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mostBooked(n, meetings)
    print("\noutput:", serialize(ans, "integer"))
