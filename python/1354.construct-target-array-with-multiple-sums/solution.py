# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isPossible(target)
    print("\noutput:", serialize(ans, "boolean"))
