# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/friends-of-appropriate-ages/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    ages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFriendRequests(ages)
    print("\noutput:", serialize(ans, "integer"))
