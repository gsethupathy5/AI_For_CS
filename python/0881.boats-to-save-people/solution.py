# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/boats-to-save-people/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    people: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numRescueBoats(people, limit)
    print("\noutput:", serialize(ans, "integer"))
