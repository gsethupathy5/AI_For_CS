# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minNumberOperations(target)
    print("\noutput:", serialize(ans, "integer"))
