# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    groupSizes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().groupThePeople(groupSizes)
    print("\noutput:", serialize(ans, "integer[][]"))
