# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().removeElement(nums, val)
    print("\noutput:", serialize(ans, "integer"))
