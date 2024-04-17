# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().movesToMakeZigzag(nums)
    print("\noutput:", serialize(ans, "integer"))
