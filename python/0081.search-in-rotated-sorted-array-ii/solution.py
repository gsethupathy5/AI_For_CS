# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)
    print("\noutput:", serialize(ans, "boolean"))
