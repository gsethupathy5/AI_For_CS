# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    times: List[List[int]] = deserialize("List[List[int]]", read_line())
    targetFriend: int = deserialize("int", read_line())
    ans = Solution().smallestChair(times, targetFriend)
    print("\noutput:", serialize(ans, "integer"))
