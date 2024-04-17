# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/patching-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().minPatches(nums, n)
    print("\noutput:", serialize(ans, "integer"))
