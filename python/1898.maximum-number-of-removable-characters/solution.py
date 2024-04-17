# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    removable: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumRemovals(s, p, removable)
    print("\noutput:", serialize(ans, "integer"))
