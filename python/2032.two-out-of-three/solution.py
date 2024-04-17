# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/two-out-of-three/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    nums3: List[int] = deserialize("List[int]", read_line())
    ans = Solution().twoOutOfThree(nums1, nums2, nums3)
    print("\noutput:", serialize(ans, "integer[]"))
