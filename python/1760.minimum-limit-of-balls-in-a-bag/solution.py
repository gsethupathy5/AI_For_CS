# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    maxOperations: int = deserialize("int", read_line())
    ans = Solution().minimumSize(nums, maxOperations)
    print("\noutput:", serialize(ans, "integer"))
