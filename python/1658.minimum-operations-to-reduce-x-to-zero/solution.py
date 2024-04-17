# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minOperations(nums, x)
    print("\noutput:", serialize(ans, "integer"))
