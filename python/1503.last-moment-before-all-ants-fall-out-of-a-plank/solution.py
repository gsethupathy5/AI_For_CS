# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    left: List[int] = deserialize("List[int]", read_line())
    right: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getLastMoment(n, left, right)
    print("\noutput:", serialize(ans, "integer"))
