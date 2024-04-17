# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reductionOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
