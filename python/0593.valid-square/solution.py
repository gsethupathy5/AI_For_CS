# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    p1: List[int] = deserialize("List[int]", read_line())
    p2: List[int] = deserialize("List[int]", read_line())
    p3: List[int] = deserialize("List[int]", read_line())
    p4: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validSquare(p1, p2, p3, p4)
    print("\noutput:", serialize(ans, "boolean"))
