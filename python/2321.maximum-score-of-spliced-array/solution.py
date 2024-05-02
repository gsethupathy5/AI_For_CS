# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-of-spliced-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        return max(sum(nums1), sum(nums2) + max(diff[i] for i in range(1, n)))

# Note: The actual implementation may vary based on the specific logic used.
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumsSplicedArray(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
