# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/advantage-shuffle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().advantageCount(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[]"))