# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pass  # Your code here.
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minOperations(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
