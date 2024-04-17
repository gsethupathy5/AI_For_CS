# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/4sum-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    nums3: List[int] = deserialize("List[int]", read_line())
    nums4: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fourSumCount(nums1, nums2, nums3, nums4)
    print("\noutput:", serialize(ans, "integer"))
